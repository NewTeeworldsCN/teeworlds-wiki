import sys, os, markdown
import shutil

def BuildWeb():
    if os.path.exists("web-build") == False:
        os.mkdir("web-build")

    # 读取模板
    file = open("example.html")
    example = file.read()
    file.close()

    if os.path.exists("web-build/resources"):
        shutil.rmtree("web-build/resources")
    shutil.copytree("resources", "web-build/resources")

    def BuildFile(name):
        # 转换HTML
        file = open(f"docs/{name}.md")
        md = file.read()
        md = md.replace(".md", ".html") # 暂时先这样判断一下（
        html = markdown.markdown(md)
        file.close()
        # 保存
        buffer = example
        buffer = buffer.format(html)
        file = open(f"web-build/{name}.html", "w")
        file.write(buffer)
        file.close()
    for file_path in os.listdir("docs"):
        file_name = os.path.splitext(file_path)[0]
        BuildFile(file_name)


def main():
    BuildWeb()

if __name__ == "__main__":
    sys.exit(main())