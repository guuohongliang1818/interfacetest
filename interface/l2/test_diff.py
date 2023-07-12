# 姓名：郭宏亮
# 时间：2023/6/27 20:09
from deepdiff import DeepDiff


def test_diff():
    t1 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": [1, 2, 3]}}
    t2 = {1: 1, 2: 2, 3: 3, 4: {"a": "hello", "b": [1, 2, 2, 3]}}
    diff = DeepDiff(t1, t2)
    print("diff", diff)
