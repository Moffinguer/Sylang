# Syl

This proyect intends to create a compiler to CLang.
To do so we are using the ANTLR tool.
TODO:
- [ ] Scope of Syl Lang
- [ ] Creation of Lexer
- [ ] Creation of Parser
- [ ] Creation of Abstract Tree
- [ ] Translator to CLang


## Sintax of Syl

Here we will define the evolution of the language

1. Version 1.0.0 _Mithrandir_: Imperative Language
```

natural number := 5;
real numberFloat := 5.2;

numberFloat := number add number sub 2 add numberFloat mul 5;

if numberFloat gt 10 or number eq 5 then
{
    print "Number evaluated"; # This comment does not appear
}

natural i = 0;
while i le 20 then
{
    #**
    # This is a commented block
    # pretty big
    #**
    print i;
}
```

### Reserved Keywords
| natural | real | if | then | while |
|:---:|:---:|:---:|:---:|:---:|
| **add** | **sub** | **mul** | **div** | **gt** |
| **lt** | **eq** | **ne** | **ge** | **le** |
| **and** | **or** | **xor** | **not** |  |


### Operators

- Addition[ **+** ]: _\<expresion>_ add _\<expresion>_
- subtract[ **-** ]: _\<expresion>_ sub _\<expresion>_ | sub _\<expresion>_
- Multiply[ **\*** ]: _\<expresion>_ mul _\<expresion>_
- Division[ **/** ]: _\<expresion>_ div _\<expresion>_
- Greater than[ **\>** ]: _\<expresion>_ gt _\<expresion>_
- Less than[ **\<** ]: _\<expresion>_ lt _\<expresion>_
- Equal to[ **==** ]: _\<expresion>_ eq _\<expresion>_
- Not equal to[ **!=** ]: _\<expresion>_ ne _\<expresion>_
- Greater than or equal to[ **\>=** ]: _\<expresion>_ ge _\<expresion>_
- Less than or equal to[ **\<=** ]: _\<expresion>_ le _\<expresion>_
- And [ **&&** ]: _\<expresion>_ and _\<expresion>_
- Or [ **||** ]: _\<expresion>_ or _\<expresion>_
- Xor [ **^** ]: _\<expresion>_ xor _\<expresion>_
- Not [ **!** ]: not _\<expresion>_

### Instructions

- Binary Conditional Estatement:
```
    if ... then
    {
        # Do something
    }
``` 
- Control Flow:
```
    while ... then
    {
        # Do something
    }
```

### Scope of language

We can group this lang on the **Imperative** class, also being **procedural** and **functional**.
TODO:
- [ ] Imperative
- [ ] Functional
- [ ] Transpiler to C
- [ ] POO





## License

**MIT License**

Copyright (c) 2023 *Moffinguer*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
