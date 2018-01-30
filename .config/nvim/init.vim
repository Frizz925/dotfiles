syntax on
filetype plugin indent on
set nocompatible
set number
set shiftwidth=4
set tabstop=4
set softtabstop=4
set termguicolors
set relativenumber
let base16colorspace=256

call plug#begin('~/.local/share/nvim/plugged')
Plug 'editorconfig/editorconfig-vim'
Plug 'chriskempson/base16-vim'
call plug#end()

if filereadable(expand("~/.vimrc_background"))
	source ~/.vimrc_background
endif
colorscheme base16-onedark
