syntax on
filetype plugin indent on
set nocompatible
set number
set shiftwidth=4
set tabstop=4
set softtabstop=4
set smartindent
set autoindent
set termguicolors
set relativenumber
set cursorline
set lazyredraw
set smartcase
set nowrap
set rtp+=~/.fzf
let base16colorspace=256

"Plugin variables
let b:vcm_tab_complete='omni'
let g:ctrlp_working_path_mode=0

if has('gui_macvim')
	set guifont=Ubuntu\ Mono\ derivative\ Powerline:h14
	"set macligatures
endif

"Pane keymaps
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"Buffer keymaps
nnoremap <C-B><C-N> :BF<CR>
nnoremap <C-B><C-P> :BB<CR>
nnoremap <C-B><C-D> :BD<CR>

"Plugin keymaps
map <C-n> :NERDTreeToggle<CR>

"Unmap things
nnoremap q <Nop>

call plug#begin('~/.vim/plugged')
Plug 'editorconfig/editorconfig-vim'
Plug 'scrooloose/nerdtree'
Plug 'tpope/vim-fugitive'
Plug 'bling/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'easymotion/vim-easymotion'
Plug 'kien/ctrlp.vim'
Plug 'ap/vim-buftabline'
Plug 'qpkorr/vim-bufkill'

if has('nvim')
	Plug 'neomake/neomake'
else
	Plug 'vim-syntastic/syntastic'
endif

"Autocompletions
"Plug 'ajh17/vimcompletesme'
"Plug 'StanAngeloff/php.vim'
"Plug 'arnaud-lb/vim-php-namespace'
"Plug 'shawncplus/phpcomplete.vim'
Plug 'Valloric/YouCompleteMe'
Plug 'lvht/phpcd.vim', { 'for': 'php', 'do': 'composer install' }
Plug '~/.fzf'

"Colorthemes
Plug 'chriskempson/base16-vim'
call plug#end()

if filereadable(expand("~/.vimrc_background"))
	source ~/.vimrc_background
endif
colorscheme base16-one-light
