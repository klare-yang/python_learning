---
tags:
  - python
---
## Function（自由函数, free function）

- 定义：不依附于任何对象、独立存在的函数
- 特点：
  - 不隐含 `self / this`
  - 通过显式参数传递数据
- 示例语言：
  - C（仅支持 free function）
  - Python / C++（同时支持）

---

## Method（对象方法, object method / member function）

- 定义：绑定在对象或类上的函数
- 特点：
  - 隐含对象本身作为第一个参数（`self` / `this`）
  - 通过 `obj.method()` 形式调用
- 示例语言：
  - Python
  - C++

---

## 语言层面对比

- C：
  - 非面向对象语言
  - 仅支持 free function
  - 不存在 method / member function

- Python / C++：
  - 支持面向对象
  - 同时存在：
    - function（如 `len(x)`）
    - method（如 `x.append()`）