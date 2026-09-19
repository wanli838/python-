# -*- coding: utf-8 -*-
"""
Python 数据类型完整教学代码
==========================================
涵盖 Python 全部内置数据类型：
    1. 数字类型: int, float, complex, bool
    2. 序列类型: str, list, tuple, range, bytes, bytearray
    3. 映射类型: dict
    4. 集合类型: set, frozenset
    5. 特殊类型: NoneType, Ellipsis
    6. 高级类型: memoryview, 类型注解

每个类型都包含：创建、访问、修改、运算、常用方法、注意事项
"""

import sys
import copy
from decimal import Decimal
from fractions import Fraction
from collections import namedtuple, OrderedDict, defaultdict, Counter, deque


def print_section(title):
    """打印分隔标题，方便阅读"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


# ==========================================================
# 第一部分：数字类型
# ==========================================================
def demo_int():
    """整数 (int) 演示"""
    print_section("1.1 整数 (int) - 任意精度整数")

    # 创建方式
    a = 10
    b = -5
    c = 0b1010       # 二进制
    d = 0o12         # 八进制
    e = 0xA          # 十六进制
    f = 1_000_000    # 下划线分隔（提高可读性）
    g = 123456789012345678901234567890  # 任意大整数

    print(f"十进制: a = {a}")
    print(f"负数: b = {b}")
    print(f"二进制: 0b1010 = {c}")
    print(f"八进制: 0o12 = {d}")
    print(f"十六进制: 0xA = {e}")
    print(f"下划线分隔: 1_000_000 = {f}")
    print(f"大整数: g = {g}")
    print(f"类型: {type(a)}")

    # 运算
    print(f"\n--- 整数运算 ---")
    print(f"10 + 3 = {10 + 3}")
    print(f"10 - 3 = {10 - 3}")
    print(f"10 * 3 = {10 * 3}")
    print(f"10 / 3 = {10 / 3}   (结果永远是float)")
    print(f"10 // 3 = {10 // 3} (整除)")
    print(f"10 % 3 = {10 % 3}   (取余)")
    print(f"10 ** 3 = {10 ** 3} (幂运算)")
    print(f"abs(-10) = {abs(-10)}")
    print(f"divmod(10, 3) = {divmod(10, 3)}")

    # 常用方法
    print(f"\n--- 常用方法 ---")
    print(f"(10).bit_length() = {(10).bit_length()}")  # 二进制位数
    print(f"(255).to_bytes(2, 'big') = {(255).to_bytes(2, 'big')}")
    print(f"int('100') = {int('100')}")
    print(f"int('0b1010', 2) = {int('0b1010', 2)}")
    print(f"int('0xFF', 16) = {int('0xFF', 16)}")

    # 注意
    print(f"\n⚠️ 注意：Python int 无溢出限制！sys.maxsize = {sys.maxsize}")


def demo_float():
    """浮点数 (float) 演示"""
    print_section("1.2 浮点数 (float) - 双精度浮点数")

    a = 3.14159
    b = -0.5
    c = 2.5e-3       # 科学计数法
    d = 1.0
    e = float('inf')  # 无穷大
    f = float('nan')  # 非数字

    print(f"a = {a}, 类型: {type(a)}")
    print(f"b = {b}")
    print(f"科学计数法 2.5e-3 = {c}")
    print(f"无穷大 = {e}")
    print(f"NaN = {f}")

    # 精度问题
    print(f"\n--- 浮点数精度问题 ---")
    print(f"0.1 + 0.2 = {0.1 + 0.2}")
    print(f"0.1 + 0.2 == 0.3 ? {0.1 + 0.2 == 0.3}")
    print(f"Decimal('0.1') + Decimal('0.2') = {Decimal('0.1') + Decimal('0.2')}")
    print(f"Fraction(1, 10) + Fraction(2, 10) = {Fraction(1, 10) + Fraction(2, 10)}")

    # 特殊判断
    print(f"\n--- 特殊值判断 ---")
    print(f"float('inf') > 1e308 = {float('inf') > 1e308}")
    print(f"float('nan') == float('nan') = {float('nan') == float('nan')}")
    import math
    print(f"math.isnan(float('nan')) = {math.isnan(float('nan'))}")
    print(f"math.isinf(float('inf')) = {math.isinf(float('inf'))}")

    # 常用方法
    print(f"\n--- 常用方法 ---")
    print(f"round(3.14159, 2) = {round(3.14159, 2)}")
    print(f"int(3.9) = {int(3.9)}  (截断)")
    print(f"float('3.14') = {float('3.14')}")
    print(f"3.14.is_integer() = {3.14.is_integer()}")
    print(f"3.0.is_integer() = {3.0.is_integer()}")


def demo_complex():
    """复数 (complex) 演示"""
    print_section("1.3 复数 (complex)")

    a = 3 + 4j
    b = complex(1, 2)
    print(f"a = {a}, 类型: {type(a)}")
    print(f"b = {b}")
    print(f"实部: a.real = {a.real}")
    print(f"虚部: a.imag = {a.imag}")
    print(f"共轭: a.conjugate() = {a.conjugate()}")
    print(f"模长: abs(a) = {abs(a)}")
    print(f"运算: (3+4j) + (1+2j) = {(3+4j) + (1+2j)}")
    print(f"运算: (3+4j) * (1+2j) = {(3+4j) * (1+2j)}")


def demo_bool():
    """布尔值 (bool) 演示"""
    print_section("1.4 布尔值 (bool) - int的子类")

    t = True
    f = False

    print(f"t = {t}, 类型: {type(t)}")
    print(f"f = {f}, 类型: {type(f)}")
    print(f"issubclass(bool, int) = {issubclass(bool, int)}")

    # 运算
    print(f"\n--- 布尔运算 ---")
    print(f"t and f = {t and f}")
    print(f"t or f = {t or f}")
    print(f"not t = {not t}")
    print(f"t + 1 = {t + 1}  (True == 1)")
    print(f"f * 5 = {f * 5}  (False == 0)")

    # 真值判断
    print(f"\n--- 真值判断 (哪些是False?) ---")
    false_values = [False, 0, 0.0, 0j, '', [], (), {}, set(), None]
    for v in false_values:
        print(f"  bool({v!r}) = {bool(v)}")

    print(f"\n--- 真值示例 ---")
    print(f"bool('False') = {bool('False')}  (非空字符串为True)")
    print(f"bool([0]) = {bool([0])}  (非空列表为True)")


# ==========================================================
# 第二部分：序列类型
# ==========================================================
def demo_str():
    """字符串 (str) 演示"""
    print_section("2.1 字符串 (str) - 不可变Unicode序列")

    # 创建方式
    s1 = 'Hello'
    s2 = "World"
    s3 = """多行
字符串"""
    s4 = r"C:\Users\test"        # 原始字符串
    s5 = b"bytes"                # 字节串（bytes类型）
    s6 = "中文 also unicode"

    print(f"s1 = {s1}")
    print(f"s4 (原始字符串) = {s4}")
    print(f"s6 = {s6}")

    # 索引与切片
    print(f"\n--- 索引与切片 ---")
    print(f"s1[0] = {s1[0]}, s1[-1] = {s1[-1]}")
    print(f"s1[1:4] = {s1[1:4]}")
    print(f"s1[:3] = {s1[:3]}")
    print(f"s1[::2] = {s1[::2]}")
    print(f"s1[::-1] = {s1[::-1]}  (反转)")

    # 运算
    print(f"\n--- 运算 ---")
    print(f"s1 + ' ' + s2 = {s1 + ' ' + s2}")
    print(f"s1 * 2 = {s1 * 2}")
    print(f"'H' in s1 = {'H' in s1}")
    print(f"len(s1) = {len(s1)}")

    # 常用方法
    print(f"\n--- 常用方法 ---")
    text = "  Hello World  "
    print(f"strip() = '{text.strip()}'")
    print(f"upper() = '{s1.upper()}'")
    print(f"lower() = '{s1.lower()}'")
    print(f"replace('H','J') = '{s1.replace('H','J')}'")
    print(f"split(' ') = {'Hello World'.split(' ')}")
    print(f"'-'.join(['a','b','c']) = {'-'.join(['a','b','c'])}")
    print(f"find('l') = {s1.find('l')}")
    print(f"count('l') = {s1.count('l')}")
    print(f"startswith('He') = {s1.startswith('He')}")
    print(f"endswith('lo') = {s1.endswith('lo')}")

    # 格式化
    print(f"\n--- 字符串格式化 ---")
    name, age = "Alice", 20
    print(f"f-string: 我叫{name}，今年{age}岁")
    print(f"format: 我叫{}，今年{}岁".format(name, age))
    print(f"%格式化: 我叫%s，今年%d岁" % (name, age))
    print(f"对齐: |{'hello':<10}|{'hello':>10}|{'hello':^10}|")
    print(f"数字: {3.14159:.2f}, 百分比: {0.25:.1%}")


def demo_list():
    """列表 (list) 演示"""
    print_section("2.2 列表 (list) - 可变序列")

    # 创建
    a = [1, 2, 3]
    b = list(range(5))
    c = [i**2 for i in range(5)]        # 列表推导式
    d = [[1, 2], [3, 4]]                # 嵌套列表
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")

    # 增删改查
    print(f"\n--- 增删改查 ---")
    fruits = ['apple', 'banana']
    fruits.append('cherry')
    print(f"append后: {fruits}")
    fruits.insert(1, 'blueberry')
    print(f"insert后: {fruits}")
    fruits.extend(['date', 'elderberry'])
    print(f"extend后: {fruits}")
    fruits.remove('banana')
    print(f"remove后: {fruits}")
    popped = fruits.pop()
    print(f"pop后: {fruits}, 弹出: {popped}")
    fruits[0] = 'APPLE'
    print(f"修改后: {fruits}")

    # 排序
    print(f"\n--- 排序 ---")
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"原: {nums}")
    print(f"sorted: {sorted(nums)}")
    print(f"sorted降序: {sorted(nums, reverse=True)}")
    nums.sort()
    print(f"sort后: {nums}")

    # 常用方法
    print(f"\n--- 常用方法 ---")
    print(f"len: {len(nums)}")
    print(f"max: {max(nums)}, min: {min(nums)}, sum: {sum(nums)}")
    print(f"index(4): {nums.index(4)}")
    print(f"count(1): {nums.count(1)}")
    nums.reverse()
    print(f"reverse后: {nums}")

    # 列表推导式
    print(f"\n--- 列表推导式 ---")
    print(f"平方: {[x**2 for x in range(5)]}")
    print(f"偶数: {[x for x in range(10) if x % 2 == 0]}")
    print(f"嵌套: {[(x,y) for x in range(2) for y in range(2)]}")

    # 浅拷贝 vs 深拷贝
    print(f"\n--- 浅拷贝 vs 深拷贝 ---")
    original = [[1, 2], [3, 4]]
    shallow = original.copy()       # 或 original[:] 或 list(original)
    deep = copy.deepcopy(original)
    original[0][0] = 999
    print(f"original = {original}")
    print(f"shallow = {shallow}  (内层被影响)")
    print(f"deep = {deep}  (完全独立)")


def demo_tuple():
    """元组 (tuple) 演示"""
    print_section("2.3 元组 (tuple) - 不可变序列")

    a = (1, 2, 3)
    b = 1, 2, 3           # 省略括号
    c = (42,)             # 单元素必须加逗号
    d = tuple(range(3))
    e = ()                # 空元组

    print(f"a = {a}, 类型: {type(a)}")
    print(f"b = {b}")
    print(f"c = {c}, 类型: {type(c)}")
    print(f"d = {d}")
    print(f"e = {e}")

    # 操作
    print(f"\n--- 操作 ---")
    print(f"索引: a[0] = {a[0]}, a[-1] = {a[-1]}")
    print(f"切片: a[1:] = {a[1:]}")
    print(f"拼接: a + d = {a + d}")
    print(f"重复: a * 2 = {a * 2}")
    print(f"长度: len(a) = {len(a)}")
    print(f"成员: 2 in a = {2 in a}")
    print(f"count: a.count(1) = {a.count(1)}")
    print(f"index: a.index(2) = {a.index(2)}")

    # 元组解包
    print(f"\n--- 元组解包 ---")
    x, y, z = a
    print(f"x, y, z = {x}, {y}, {z}")

    first, *rest = (1, 2, 3, 4, 5)
    print(f"first = {first}, rest = {rest}")

    *init, last = (1, 2, 3, 4, 5)
    print(f"init = {init}, last = {last}")

    # 交换变量
    p, q = 1, 2
    p, q = q, p
    print(f"交换后: p = {p}, q = {q}")

    # namedtuple
    print(f"\n--- namedtuple ---")
    Point = namedtuple('Point', ['x', 'y'])
    pt = Point(3, 4)
    print(f"pt = {pt}, pt.x = {pt.x}, pt.y = {pt.y}")

    print(f"\n⚠️ 注意：元组不可变，但里面的可变元素可以修改")
    t = ([1, 2], 3)
    t[0].append(999)
    print(f"t = {t}")


def demo_range():
    """range 演示"""
    print_section("2.4 range - 不可变数字序列")

    r1 = range(5)
    r2 = range(1, 10)
    r3 = range(0, 10, 2)
    r4 = range(10, 0, -1)

    print(f"range(5) = {list(r1)}")
    print(f"range(1, 10) = {list(r2)}")
    print(f"range(0, 10, 2) = {list(r3)}")
    print(f"range(10, 0, -1) = {list(r4)}")

    print(f"\n--- 特性 ---")
    print(f"len(range(5)) = {len(range(5))}")
    print(f"range(5)[2] = {range(5)[2]}")
    print(f"range(10)[2:5] = {list(range(10)[2:5])}")
    print(f"5 in range(10) = {5 in range(10)}")
    print(f"内存效率: range(1000000) 占用很少内存")

    # 应用
    print(f"\n--- 应用 ---")
    print(f"sum(range(101)) = {sum(range(101))}  (1到100的和)")
    for i in range(3):
        print(f"  第{i+1}次循环")


def demo_bytes():
    """字节串 (bytes, bytearray) 演示"""
    print_section("2.5 字节串 (bytes, bytearray)")

    b1 = b'hello'
    b2 = bytes([104, 101, 108, 108, 111])
    b3 = 'hello'.encode('utf-8')
    b4 = '中文'.encode('utf-8')

    print(f"b1 = {b1}, 类型: {type(b1)}")
    print(f"b2 = {b2}")
    print(f"b3 = {b3}")
    print(f"b4 (中文utf-8) = {b4}")

    # 解码
    print(f"\n--- 编码/解码 ---")
    print(f"b1.decode() = {b1.decode()}")
    print(f"b4.decode('utf-8') = {b4.decode('utf-8')}")

    # bytearray（可变）
    print(f"\n--- bytearray（可变字节串）---")
    ba = bytearray(b'hello')
    ba[0] = 72  # 'H'
    print(f"ba = {ba}")

    # 常用方法
    print(f"\n--- 常用方法 ---")
    print(f"b1[0] = {b1[0]}  (返回int)")
    print(f"b1[0:2] = {b1[0:2]}  (返回bytes)")
    print(f"len(b1) = {len(b1)}")
    print(f"b'hello'.hex() = {b'hello'.hex()}")


# ==========================================================
# 第三部分：映射类型
# ==========================================================
def demo_dict():
    """字典 (dict) 演示"""
    print_section("3.1 字典 (dict) - 键值对映射")

    # 创建方式
    d1 = {'name': 'Alice', 'age': 20}
    d2 = dict(name='Bob', age=25)
    d3 = dict([('a', 1), ('b', 2)])
    d4 = {x: x**2 for x in range(5)}   # 字典推导式
    d5 = {}                             # 空字典

    print(f"d1 = {d1}")
    print(f"d2 = {d2}")
    print(f"d3 = {d3}")
    print(f"d4 = {d4}")

    # 增删改查
    print(f"\n--- 增删改查 ---")
    student = {'name': 'Alice', 'age': 20}
    student['major'] = 'CS'              # 增
    print(f"增加后: {student}")
    student['age'] = 21                  # 改
    print(f"修改后: {student}")
    del student['major']                 # 删
    print(f"删除后: {student}")

    print(f"\n--- 访问 ---")
    print(f"student['name'] = {student['name']}")
    print(f"student.get('age') = {student.get('age')}")
    print(f"student.get('xxx', 'default') = {student.get('xxx', 'default')}")

    # 遍历
    print(f"\n--- 遍历 ---")
    print("遍历键:", end=" ")
    for k in student.keys():
        print(k, end=" ")
    print()
    print("遍历值:", end=" ")
    for v in student.values():
        print(v, end=" ")
    print()
    print("遍历键值对:")
    for k, v in student.items():
        print(f"  {k}: {v}")

    # 常用方法
    print(f"\n--- 常用方法 ---")
    d = {'a': 1, 'b': 2}
    print(f"keys() = {list(d.keys())}")
    print(f"values() = {list(d.values())}")
    print(f"items() = {list(d.items())}")
    print(f"pop('a') = {d.pop('a')}, 剩余 = {d}")
    d.update({'c': 3, 'd': 4})
    print(f"update后: {d}")
    print(f"setdefault('e', 5) = {d.setdefault('e', 5)}")
    d.clear()
    print(f"clear后: {d}")

    # 合并运算符 (Python 3.9+)
    print(f"\n--- 合并 (Python 3.9+) ---")
    a = {'x': 1}
    b = {'y': 2}
    print(f"a | b = {a | b}")

    # 特殊字典
    print(f"\n--- 特殊字典 ---")
    od = OrderedDict([('a', 1), ('b', 2)])
    print(f"OrderedDict: {od}")

    dd = defaultdict(list)
    dd['fruits'].append('apple')
    dd['fruits'].append('banana')
    print(f"defaultdict: {dict(dd)}")

    c = Counter('hello world')
    print(f"Counter: {c}")
    print(f"Counter.most_common(3): {c.most_common(3)}")

    # 字典的键
    print(f"\n⚠️ 注意：字典的键必须是不可变类型")
    print(f"可作键: int, str, tuple, frozenset")
    print(f"不可作键: list, dict, set")


# ==========================================================
# 第四部分：集合类型
# ==========================================================
def demo_set():
    """集合 (set) 演示"""
    print_section("4.1 集合 (set) - 无序不重复")

    # 创建
    s1 = {1, 2, 3, 4, 5}
    s2 = set([3, 4, 5, 6, 7])
    s3 = set('hello')       # 去重
    s4 = {x**2 for x in range(5)}  # 集合推导式
    s5 = set()              # 空集合（注意不能用{}）

    print(f"s1 = {s1}")
    print(f"s2 = {s2}")
    print(f"s3 = {s3}  (字符串去重)")
    print(f"s4 = {s4}")
    print(f"type({{}}) = {type({})}  (这是dict!)")
    print(f"type(set()) = {type(set())}")

    # 集合运算
    print(f"\n--- 集合运算 ---")
    print(f"并集 s1 | s2 = {s1 | s2}")
    print(f"交集 s1 & s2 = {s1 & s2}")
    print(f"差集 s1 - s2 = {s1 - s2}")
    print(f"对称差 s1 ^ s2 = {s1 ^ s2}")

    print(f"\n--- 方法形式 ---")
    print(f"union: {s1.union(s2)}")
    print(f"intersection: {s1.intersection(s2)}")
    print(f"difference: {s1.difference(s2)}")

    # 增删
    print(f"\n--- 增删 ---")
    s = {1, 2, 3}
    s.add(4)
    print(f"add(4): {s}")
    s.discard(1)
    print(f"discard(1): {s}")
    s.update([5, 6, 7])
    print(f"update([5,6,7]): {s}")
    s.remove(7)
    print(f"remove(7): {s}")

    # 关系判断
    print(f"\n--- 关系判断 ---")
    a = {1, 2}
    b = {1, 2, 3}
    print(f"{a} <= {b}? {a <= b}  (子集)")
    print(f"{b} >= {a}? {b >= a}  (超集)")
    print(f"{a}.isdisjoint({b})? {a.isdisjoint(b)}")

    # 应用：去重
    print(f"\n--- 应用：去重 ---")
    lst = [1, 2, 2, 3, 3, 3, 4]
    unique = list(set(lst))
    print(f"原列表: {lst}")
    print(f"去重后: {unique}")
    print(f"保持顺序去重: {list(dict.fromkeys(lst))}")


def demo_frozenset():
    """frozenset 演示"""
    print_section("4.2 不可变集合 (frozenset)")

    fs = frozenset([1, 2, 3, 4])
    print(f"fs = {fs}, 类型: {type(fs)}")

    # 支持的操作
    print(f"\n--- 支持的操作 ---")
    print(f"并集: {fs | frozenset([5])}")
    print(f"交集: {fs & frozenset([3, 4, 5])}")
    print(f"成员: 3 in fs = {3 in fs}")

    # 可作字典的键
    d = {fs: 'value'}
    print(f"\n可作字典键: {d}")

    # 不可变
    print(f"⚠️ 注意：frozenset 不可变，没有 add/remove 方法")


# ==========================================================
# 第五部分：特殊类型
# ==========================================================
def demo_none():
    """NoneType 演示"""
    print_section("5.1 NoneType")

    x = None
    print(f"x = {x}, 类型: {type(x)}")
    print(f"x is None = {x is None}")
    print(f"bool(None) = {bool(None)}")
    print(f"None == False ? {None == False}")
    print(f"None == 0 ? {None == 0}")

    # 应用场景
    print(f"\n--- 应用场景 ---")
    def find_item(lst, target):
        for i, item in enumerate(lst):
            if item == target:
                return i
        return None  # 未找到

    result = find_item([1, 2, 3], 5)
    if result is None:
        print("未找到")
    else:
        print(f"找到，索引为 {result}")


def demo_ellipsis():
    """Ellipsis 演示"""
    print_section("5.2 Ellipsis (...)")

    e = ...
    print(f"e = {e}, 类型: {type(e)}")
    print(f"e is Ellipsis = {e is Ellipsis}")

    # 应用场景：类型提示、numpy切片占位
    print(f"\n--- 应用场景 ---")
    print("1. 类型提示: def func(x: int) -> ...: ...")
    print("2. NumPy切片: arr[..., 0]")
    print("3. 占位符: def todo(): ...")


def demo_memoryview():
    """memoryview 演示"""
    print_section("5.3 memoryview")

    data = bytearray(b'hello world')
    mv = memoryview(data)

    print(f"data = {data}")
    print(f"mv = {mv}")
    print(f"mv[0] = {mv[0]}")
    print(f"mv[0:5] = {bytes(mv[0:5])}")

    # 零拷贝修改
    mv[0] = ord('H')
    print(f"修改后 data = {data}  (原数据被修改)")

    print(f"\n用途：高效处理大块二进制数据，避免拷贝")


# ==========================================================
# 第六部分：类型转换与判断
# ==========================================================
def demo_type_conversion():
    """类型转换演示"""
    print_section("6.1 类型转换")

    # 数字 ↔ 字符串
    print(f"int('123') = {int('123')}")
    print(f"float('3.14') = {float('3.14')}")
    print(f"str(456) = '{str(456)}'")
    print(f"str(3.14) = '{str(3.14)}'")

    # 数字 ↔ 数字
    print(f"int(3.9) = {int(3.9)}  (截断)")
    print(f"float(5) = {float(5)}")
    print(f"complex(1, 2) = {complex(1, 2)}")
    print(f"bool(0) = {bool(0)}")
    print(f"bool(1) = {bool(1)}")

    # 序列转换
    print(f"\n--- 序列转换 ---")
    print(f"list('abc') = {list('abc')}")
    print(f"tuple([1,2,3]) = {tuple([1,2,3])}")
    print(f"set([1,2,2,3]) = {set([1,2,2,3])}")
    print(f"list(range(3)) = {list(range(3))}")
    print(f"dict([('a',1),('b',2)]) = {dict([('a',1),('b',2)])}")

    # 字符串 ↔ 字节
    print(f"\n--- 字符串 ↔ 字节 ---")
    s = 'hello 中文'
    b = s.encode('utf-8')
    print(f"encode: {b}")
    print(f"decode: {b.decode('utf-8')}")


def demo_type_check():
    """类型判断演示"""
    print_section("6.2 类型判断")

    values = [42, 3.14, 2+3j, True, 'hello', b'bytes', [1,2], (1,2), {1,2}, {'a':1}, None]

    print(f"{'值':<15} {'type()':<15} {'isinstance':<20}")
    print("-" * 50)
    for v in values:
        print(f"{repr(v):<15} {str(type(v).__name__):<15} {str(isinstance(v, (int, float))):<20}")

    print(f"\n--- isinstance vs type ---")
    print(f"isinstance(True, int) = {isinstance(True, int)}  (bool是int子类)")
    print(f"type(True) == int = {type(True) == int}  (类型不等)")
    print(f"isinstance(True, bool) = {isinstance(True, bool)}")
    print(f"isinstance(True, (int, float)) = {isinstance(True, (int, float))}")


def demo_mutable_immutable():
    """可变 vs 不可变类型"""
    print_section("6.3 可变 vs 不可变类型")

    print("【不可变类型】: int, float, complex, bool, str, tuple, frozenset, bytes")
    print("【可变类型】: list, dict, set, bytearray")

    # 不可变示例
    print(f"\n--- 不可变类型 ---")
    s = "hello"
    s2 = s
    s = s + " world"  # 创建新对象
    print(f"s = {s}")
    print(f"s2 = {s2}  (不受影响)")
    print(f"id(s) != id(s2): {id(s) != id(s2)}")

    # 可变示例
    print(f"\n--- 可变类型 ---")
    lst = [1, 2, 3]
    lst2 = lst
    lst.append(4)  # 原地修改
    print(f"lst = {lst}")
    print(f"lst2 = {lst2}  (被影响!)")
    print(f"id(lst) == id(lst2): {id(lst) == id(lst2)}")

    # 函数传参
    print(f"\n--- 函数传参陷阱 ---")
    def modify_list(x):
        x.append(999)

    def modify_int(x):
        x = 999

    my_list = [1, 2, 3]
    modify_list(my_list)
    print(f"list传参后: {my_list}  (被修改)")

    my_int = 1
    modify_int(my_int)
    print(f"int传参后: {my_int}  (未修改)")


# ==========================================================
# 第七部分：高级容器
# ==========================================================
def demo_advanced_containers():
    """高级容器演示"""
    print_section("7.1 collections 模块高级容器")

    # deque 双端队列
    from collections import deque
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(f"deque: {dq}")
    print(f"popleft: {dq.popleft()}, pop: {dq.pop()}")
    print(f"剩余: {dq}")

    # Counter 计数器
    from collections import Counter
    c = Counter('abracadabra')
    print(f"\nCounter: {c}")
    print(f"most_common(2): {c.most_common(2)}")

    # defaultdict
    from collections import defaultdict
    dd = defaultdict(int)
    for ch in 'abracadabra':
        dd[ch] += 1
    print(f"\ndefaultdict: {dict(dd)}")

    # namedtuple
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(3, 4)
    print(f"\nnamedtuple: {p}, p.x = {p.x}")

    # OrderedDict
    from collections import OrderedDict
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    print(f"\nOrderedDict: {od}")


# ==========================================================
# 主函数
# ==========================================================
def main():
    """主函数"""
    print("=" * 60)
    print("  Python 数据类型完整教学")
    print("=" * 60)
    print("""
本程序涵盖以下数据类型：
    1. 数字类型: int, float, complex, bool
    2. 序列类型: str, list, tuple, range, bytes, bytearray
    3. 映射类型: dict
    4. 集合类型: set, frozenset
    5. 特殊类型: NoneType, Ellipsis, memoryview
    6. 类型转换与判断
    7. 高级容器: deque, Counter, defaultdict, namedtuple, OrderedDict
    """)
    input("按回车键开始...")

    # 1. 数字类型
    demo_int()
    demo_float()
    demo_complex()
    demo_bool()

    input("\n继续看序列类型？按回车...")

    # 2. 序列类型
    demo_str()
    demo_list()
    demo_tuple()
    demo_range()
    demo_bytes()

    input("\n继续看映射与集合类型？按回车...")

    # 3. 映射类型
    demo_dict()

    # 4. 集合类型
    demo_set()
    demo_frozenset()

    input("\n继续看特殊类型与类型转换？按回车...")

    # 5. 特殊类型
    demo_none()
    demo_ellipsis()
    demo_memoryview()

    # 6. 类型转换与判断
    demo_type_conversion()
    demo_type_check()
    demo_mutable_immutable()

    input("\n继续看高级容器？按回车...")

    # 7. 高级容器
    demo_advanced_containers()

    print_section("教学结束")
    print("""
📝 总结：
    不可变类型: int, float, complex, bool, str, tuple, frozenset, bytes, NoneType
    可变类型:   list, dict, set, bytearray
    
    常用转换: int() float() str() bool() list() tuple() set() dict()
    类型判断: type(x)  isinstance(x, Type)
    
💡 建议：修改代码中的示例，亲自尝试各种操作！
    """)


if __name__ == "__main__":
    main()
