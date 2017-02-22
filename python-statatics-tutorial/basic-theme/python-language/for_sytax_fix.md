---
author : 高峰
---
本节主要内容：
* [基本使用](#m1)
* [实例](#m2)
* [进阶](#m3)
* [高级主题](#m4)

在上一讲中我们学习了 while 语句进行循环控制，接下来我们将要学习另一种循环语句 for 。

<h4 class="tut-h4-pad" id="m1">基本使用</h4>
不同编程语言都有 for 语言，比如 C# 语言中的 **foreach**, Java 语言中的 **for**,在 Python
中的基本使用方法如下。
```python
for item in sequence:
    expressions
```
`sequence` 为可迭代的对象，`item` 为序列中的每个对象。

<h4 class="tut-h4-pad" id="m2">实例</h4>
```python
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)
```
输出的结果为 `1,2,3,4,5,6,7,12,543,876,12,3,2,5`, 内容依次为 `example_list` 中的每一个元素
注意 Python 是使用缩进表示程序的结构，如果程序这样编写，
```python
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)
    print('inner of for')
print('outer of for')
```
那么每次循环都会输出 `inner of for`,在循环结束后，输出 `outer of for` 一次。


<h4 class="tut-h4-pad" id="m3">进阶</h4>
#### range使用

在 Python 内置了工厂函数，`range` 函数将会返回一个序列，总共有三种使用方法
##### 1 range(start, stop)

其中 `start` 将会是序列的起始值，`stop`为结束值，但是**不包括**该值，类似
数学中的表达 `[start, stop)`,左边为闭区间，右边为开区间。
```python
for i in range(1, 10):
    print(i)
```
上述表达将会返回 `1-9` 所有整数，但不包含 `10`
##### 2 range(stop)

如果省略了 `start` 那么将从 **0** 开始，相当于 `range(0, stop)`

##### 3 range(start, stop, step)
`step` 代表的为步长，即相隔的两个值得差值。从 `start` 开始，依次增加
`step` 的值，直至**等于或者大于** `stop`
```python
for i in range(0,13, 5):
    print(i)
```
将会输出 `0, 5, 10`。


<h4 class="tut-h4-pad" id="m4">高级主题</h4>
#### 4.1 内置集合
Python 共内置了 `list`、 `tuple` 、`dict` 和 `set` 四种基本集合，每个
集合对象都能够迭代。
##### tuple 类型

```python
tup = ('python', 2.7, 64)
for i in tup:
    print(i)
```
程序将以此按行输出 'python', 2.7 和 64。

##### dictionary 类型

```python
dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
    print(key, dic[key])
```
输出的结果为：`platform 64，lan python, version 2.7`, 字典在迭代的过程
中将 `key` 作为可迭代的对象返回。注意字典中 `key` 是乱序的，也就是说和插入
的顺序是不一致的。如果想要使用顺序一致的字典，请使用 `collections` 模块
中的 `OrderedDict` 对象。

##### set 类型

```python
s = set(['python', 'python2', 'python3','python'])
for item in s:
    print(item)
```
将会输出 `python, python3, python2` set 集合将会去除重复项，注意输出的
结果也不是按照输入的顺序。

#### 4.2 迭代器
Python 中的 `for` 句法实际上实现了设计模式中的[迭代器模式](https://en.wikipedia.org/wiki/Iterator_pattern#Python)
，所以我们自己也可以按照迭代器的要求自己生成迭代器对象，以便在 `for` 语句中使用。
只要类中实现了 `__iter__` 和 `next` 函数，那么对象就可以在 `for` 语句中使用。
现在创建 Fibonacci 迭代器对象,
```python
# define a Fib class
class Fib(object): 
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 

    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()

# using Fib object
for i in Fib(5):
    print(i)
```
将会输出前 5 个 Fibonacci 数据 `1，1, 2, 3, 5`

#### 4.3 生成器
除了使用迭代器以外，Python 使用 `yield` 关键字也能实现类似迭代的效果，`yield` 语句每次
执行时，立即返回结果给上层调用者，而当前的状态仍然保留，以便迭代器下一次循环调用。这样做的
好处是在于节约硬件资源，在需要的时候才会执行，并且每次只执行一次。
```python
def fib(max):
    a, b = 0, 1
    while max:
        r = b
        a, b = b, a+b
        max -= 1
        yield r

# using generator
for i in fib(5):
    print(i)
```
将会输出前 5 个 Fibonacci 数据 `1，1, 2, 3, 5`