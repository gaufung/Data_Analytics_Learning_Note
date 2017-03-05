---
author : 高峰
---

本节主要内容：
* [基本使用](#m1)
* [实例](#m2)

如果我们用代码实现了一个小功能，但想要在程序代码中重复使用，不能在代码中到处粘贴这些代码，因为这样做违反
了软件工程中 [DRY原则](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)。 Python 提供了
**函数**功能，可以将我们这部分功能抽象成一个函数以方便程序调用，或者提供给其他模块使用。

<h4 class="tut-h4-pad" id="m1">基本使用</h4>

```python
def function_name(parameters):
    expressions
```
Python 使用 `def` 开始函数定义，紧接着是函数名，括号内部为函数的参数，内部为函数的
具体功能实现代码，如果想要函数有返回值, 在 `expressions` 中的逻辑代码中用 `return` 返回。

<h4 class="tut-h4-pad" id="m2">实例</h4>

```python
def function():
    print('This is a function')
    a = 1+2
    print(a)
```

上面我们定义了一个名字为 `function` 的函数，函数没有不接受参数，所以括号内部为空，紧接着就是
函数的功能代码。如果执行该脚本，发现并没有输出任何输出，因为我们只定义了函数，而并没有执行函数。
这时我们在 Python 命令提示符中输入函数调用 `function()`, 注意这里调用函数的括号不能省略。那么
函数内部的功能代码将会执行，输出结果：

```python
This is a function
3
```

如果我们想要在脚本中调用的脚本，只需要在脚本中最后添加函数调用语句

```python
function()
```

那么在执行脚本的时候，将会执行函数。