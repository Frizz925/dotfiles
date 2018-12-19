from i3lemonbar import Block, Scheduler
from i3lemonbar.containers import inject

import codecs
import time
import subprocess


class BatteryInfo(object):
    def __init__(self, text: str):
        self.level = self._parse_level(text)
        self.status = self._parse_status(text)

    def _parse_level(self, text: str) -> float:
        levels = []
        for line in text.splitlines():
            # Get the 2nd token of the line, remove last character, cast to int
            level = int(line.split(',')[1][:-1])
            levels.append(level)
        return sum(levels) / len(levels)

    def _parse_status(self, text: str) -> str:
        return text.split(',')[0] \
            .split(':')[1] \
            .strip()


@inject(Scheduler)
class Battery(Block):
    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler
        self.acpi_exists = True

    def should_update(self):
        # only update every 60 seconds
        return self.acpi_exists and round(time.time()) % 60 == 0

    def render(self):
        acpi = None
        try:
            acpi = subprocess.Popen(
                ['acpi', 'battery'],
                stdout=subprocess.PIPE,
                stderr=self.scheduler.stderr,
            )
        except FileNotFoundError:
            self.acpi_exists = False
            return ''

        res = acpi.communicate()[0]
        if len(res) <= 0:
            return ''
        res_text = codecs.decode(res, 'utf-8')
        battery = BatteryInfo(res_text)

        icon = '\uf244'
        if battery.status == 'Charging':
            icon = '\uf0e7'
        elif battery.level > 80:
            icon = '\uf240'
        elif battery.level > 60:
            icon = '\uf241'
        elif battery.level > 40:
            icon = '\uf242'
        elif battery.level > 20:
            icon = '\uf243'

        return '%s  %d%%' % (icon, round(battery.level))
