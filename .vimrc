call plug#begin('~/.vim/plugged')
"Plug 'joshdick/onedark.vim'
"Plug 'sonph/onehalf', {'rtp': 'vim/'}
Plug 'rakr/vim-one'
Plug 'w0rp/ale'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'scrooloose/nerdtree'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
call plug#end()

set nocompatible
set number
set relativenumber
set softtabstop=4
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent
set modeline
set laststatus=2
set background=light

if (has("termguicolors"))
	set termguicolors
endif

let g:airline_theme='one'
let g:one_allow_italics=1
let g:airline_powerline_fonts=1
let g:deoplete#enable_at_startup=1
colorscheme one

map <C-n> :NERDTreeToggle<CR>
