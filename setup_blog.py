import os

def setup_blog():
    # 1. إنشاء ملف الإعدادات للقالب
    with open("_config.yml", "w") as f:
        f.write("theme: jekyll-theme-minima\n")
        f.write("title: Dobli Blog\n")
        f.write("description: My automated AI-driven blog\n")
    
    # 2. إنشاء مجلد المقالات إذا لم يكن موجوداً
    if not os.path.exists("_posts"):
        os.makedirs("_posts")
        print("تم إنشاء مجلد _posts")

    # 3. رفع الإعدادات الجديدة لـ GitHub
    os.system("git add .")
    os.system('git commit -m "Automated setup: Jekyll theme and blog structure"')
    os.system("git push origin main")
    print("تمت تهيئة المدونة تلقائياً بنجاح!")

if __name__ == "__main__":
    setup_blog()
