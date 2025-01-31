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

    def BuildFile(path, file_name, output_name=""):
        file_extension = os.path.splitext(file_name)[1]
        if file_extension != ".md":
            print(f"file '{file_name}' is not a markdown file! Its extension is '{file_extension}'")
            return
        if output_name == "":
            output_name = os.path.splitext(file_name)[0]
        # 转换HTML
        if path == "":
            file = open(file_name)
        else:
            file = open(f"{path}/{file_name}")
        md = file.read()
        md = md.replace(".md", ".html") # 暂时先这样判断一下（
        html = markdown.markdown(md, extensions=["tables", "fenced_code"])
        file.close()
        # 保存
        buffer = example
        buffer = buffer.format(html)
        file = open(f"web-build/{output_name}.html", "w")
        file.write(buffer)
        file.close()
    for file_path in os.listdir("docs"):
        BuildFile("docs", file_path)
    BuildFile("", "README.md", "about")


def main():
    BuildWeb()

if __name__ == "__main__":
    sys.exit(main())