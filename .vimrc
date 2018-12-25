
call plug#begin('~/.vim/plugged')
"Look and feel
"Plug 'rakr/vim-one'
"Plug 'arcticicestudio/nord-vim'
Plug 'chriskempson/base16-vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

"Autocompletions
Plug 'lvht/phpcd.vim', { 'for': 'php', 'do': 'composer install' }
if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif

"Extras
Plug 'neomake/neomake'
call plug#end()

set nocompatible
set relativenumber
set smartcase
set smarttab
set expandtab
set softtabstop=4
set shiftwidth=4
set tabstop=4
set autoindent
set background=dark
set listchars=nbsp:¬,tab:>-,extends:»,precedes:«,space:•,trail:•
set modeline
set modelines=5
set termguicolors
"set list

let base16colorspace=256
let g:airline_theme = 'base16'
let g:one_allow_italics = 1
let g:python_host_prog = '/usr/local/bin/python'
let g:python3_host_prog = '/usr/local/bin/python3'
let g:phpcd_php_cli_executable = '/usr/local/bin/php'
let g:deoplete#enable_at_startup = 1
let g:deoplete#ignore_sources = get(g:, 'deoplete#ignore_sources', {})
let g:deoplete#ignore_sources.php = ['omni']

filetype off
filetype plugin indent on
syntax on
colorscheme base16-material-darker

call neomake#configure#automake('nw', 750)
"call one#highlight('Normal', '', 'ffffff', '')

"Autocmds
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab
