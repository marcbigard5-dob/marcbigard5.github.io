import os

def publish_article(filename, content):
    # 1. كتابة المحتوى في ملف
    with open(filename, "w") as f:
        f.write(content)
    
    # 2. تنفيذ أوامر Git للرفع تلقائياً
    os.system("git add .")
    os.system('git commit -m "Auto-publish post from Dobli Agent"')
    os.system("git push origin main")
    print("تم رفع المقال بنجاح إلى GitHub!")

# مثال للاستخدام:
if __name__ == "__main__":
    publish_article("post1.md", "# عنوان المقال\nهذا هو محتوى المقال التلقائي من Dobli.")
