# 姓名：郭宏亮
# 时间：2023/6/15 21:42
import os

import yaml


class GetEnv:

    @classmethod
    def get_env(cls):
        env = os.getenv("litemall_env", default="dev")
        print("env", env)
        print(os.path.abspath(f"{env}.yaml"))
        # 路径优化
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{env}.yaml")
        print(path)
        with open(path, "r", encoding="utf-8") as f:
            env_config = yaml.safe_load(f)
        print("env_config", env_config)
        return env_config


if __name__ == '__main__':
    GetEnv.get_env()
