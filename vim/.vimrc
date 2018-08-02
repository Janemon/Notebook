:function Me()
:  echom "hello!"
:endfunction

:function Nme()
:  return "New hi"
:endfunction

:function NoReturn()
:endfunction

:function DisplayName(name)
   echom "Hello, your name is: "
   echom a:name
:endfunction

:function NewD(nname)
   echom "Hi, your name is "
   echom nname
:endfunction

:function VArg(...)
   echom a:0
   echom a:1
   echo  a:000
:endfunction

:function Nvarg(foo, ...)
   echom a:foo
   echom a:0
   echom a:1
   echom a:2
   echo  a:000
:endfunction

:function Assign(efoo)
   let a:efoo="Nope"
   echom a:efoo
:endfunction

:function AssignN(foon)
   let foon_tmp=a:foon
   let foon_tmp="Yep"
   echom foon_tmp
:endfunction

:function Conc()
   echom "hell, "."World!"
:endfunction

:function Chang()
   echo "foo\nbar"
:endfunction

:function Literal()
   echom '\n, right?'
   echom 'That''s right?'
:endfunction
