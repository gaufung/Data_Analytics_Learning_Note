---
author : 高峰
---

本节主要内容：
* [基本使用](#m1)
* [实例](#m2)
* [注意点](#m3)

除了常见的循环控制语句，Python 中还有 `if`, `if else` 和 `if elif` 等判断语句，本讲将简单介绍 `if` 语句

<h4 class="tut-h4-pad" id="m1">基本使用</h4>
与其他编程语言中的 `if` 语句一样，使用方法如下
```python
if condition:
    expressions
``` 
如果 `condition` 的值为 `True`,将会执行 `expressions` 语句的内容，否则将跳过该语句往下执行。

<h4 class="tut-h4-pad" id="m2">实例</h4>
```python
x = 1 
y = 2
z = 3
if x < y:
    print('x is less than y')
```
上述代码中，`if` 语句的条件为 `x < y` 为 `True`, 那么将执行条件内部语句，程序将输出 `x is less than y`。
当我们将代码修改为一下
```python
if x < y < z:
    print('x is less than y, and y is less than z')
```
在这里的条件变成了 `x < y < z`, 其相当于 `x < y and y < z`, 如果 `and` 两边的条件都为 `True` 那么才会返回 `True`。
注意这个用法是 python 语言特有，**不鼓励** 大家写出这样的代码，以便其他语言的程序员能够看懂你的代码。

<h4 class="tut-h4-pad" id="m3">注意点</h4>
在 python 语言中等号的判断使用 `==` 而不是 `=`, 因为后一种是赋值语句。
```python
x = 1 
y = 2 
z = 3
if x = y:
    print('x is equal to y')
```
如果这样写的话，是有句法错误的，程序将无法执行。当然如果是从 `C/C++` 语言转过来的同学，刚才那一句是非常熟悉的，也是我们经常错误的来源。

修改如下
```python
x = 2
y = 2
z = 0
if x == y:
    print('x is equal to y')
```
因为 `x` 和 `y` 都等于2, 所以将会输出 `x is equal to y`。