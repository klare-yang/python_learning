---
tags:
  - python
---
python中，类型属于对象而非变量，故无需对数据类型进行显式定义或转换

---
##  Python 是**强类型语言**（Strongly Typed Language）

- Python **严格区分**：
    - `int‘    
    - `float`
    - `str`
    - `bool`

---

## Python 是**动态类型语言**（Dynamically Typed Language）

> **类型在运行时决定，而不是在编译时声明**

例如：
```python
x = 1
x = 1.5
x = "hello"
```

这在 Python 中是合法的，因为：
- `x` 只是一个**名字（name）**
- 类型属于右侧的对象

---

## 对比：C / C++ 的类型属于谁？

|语言|类型绑定对象|
|---|---|
|C|变量（variable）|
|C++|变量 / 对象|
|Python|对象（object）|
