---
author : 高峰
---
本节主要内容：
* [基本使用](#m1)
* [实例](#m2)

上一讲主要学习了 `if else` 内容，本讲将要学习最后一个语句 `elif`(`else if`)。
<h4 class="tut-h4-pad" id="m1">基本使用</h4>
```python
if condition1:
    true1_expressions
elif condition2:
    true2_expressions
elif condtion3:
    true3_expressions
elif ...
    ...
else:
    else_expressions
```
如果有多个判断条件，那可以通过 `elif` 语句添加多个判断条件，一旦某个条件为 `True`，那么将执行对应的 `expression`。
并在之代码执行完毕后**跳出**该 `if-elif-else` 语句块，往下执行。

<h4 class="tut-h4-pad" id="m2">实例</h4>
```python
x = 4
y = 2
z = 3
if x > 1:
    print ('x > 1')
elif x < 1:
    print('x < 1')
else:
    print('x = 1')
print('finish')
```
因为 `x = 4` 那么满足 `if` 的条件，则将输出 `x > 1` 并且跳出整个 `if-elif-else` 语句块，那么紧接着输出 `finish`。 如果将
`x = -2` 那么将满足 `elif x < 1` 这个条件，将输出 `x <1, finish`。

