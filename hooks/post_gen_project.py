import shutil
from pathlib import Path

# 此处由 cookiecutter 由各个条件传入要删除的文件或文件夹
__TO_DELETE_FILES = [
    "{% if not cookiecutter.install_as_package %}eaphone{% endif %}",
    "{% if not cookiecutter.include_sphinx %}docs{% endif %}",
    "{% if not cookiecutter.include_pytest %}tests{% endif %}",
    "{% if not cookiecutter.use_inproject_venv %}poetry.toml{% endif %}",
    "{% if not cookiecutter.enable_pre_commit %}.pre-commit-config.yaml{% endif %}",
    "{% if not cookiecutter.include_git_cliff %}cliff.toml{% endif %}",
    "{% if not cookiecutter.setup_ci %}.jenkins{% endif %}",
]

if __name__ == "__main__":
    for file in __TO_DELETE_FILES:
        # 跳过未生效的部分
        if len(file) == 0:
            continue

        p = Path(file)
        if p.is_file():
            print("将要删除文件: ", p.absolute())
            p.unlink(missing_ok=True)
        elif p.is_dir():
            print("将要删除文件夹: ", p.absolute())
            shutil.rmtree(p, ignore_errors=True)
