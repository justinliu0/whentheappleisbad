et nocursorline
set nonumber
set norelativenumber
set noshowmode
set guicursor=
set lazyredraw

let g:frame_dir='ascii'
let g:fps=25
let g:delay=1000/g:fps
let g:frames=sort(split(globpath(g:frame_dir,'*.txt'),'\n'))
let g:frames_content=[]
for f in g:frames
    call add(g:frames_content, join(readfile(f),"\n"))
endfor

function! PlayFrames()
    let l:save_cursor=getpos(".")
    let l:save_view=winsaveview()
    for i in range(len(g:frames_content))
	call setline(1,split(g:frames_content[i],"\n"))
        normal! gg
        silent! redraw
	execute 'sleep '.g:delay.'m'
    endfor
    call setpos('.',l:save_cursor)
    call winrestview(l:save_view)
endfunction

call PlayFrames()

