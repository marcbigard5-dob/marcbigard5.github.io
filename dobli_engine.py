import os
import sys
from datetime import datetime
import random # للمحاكاة حتى تربط الـ API

# الوكيل A: يقوم بجلب المنتج تلقائياً بدون تدخل منك
def agent_a_research():
    print("Agent A: Fetching 'Best Sellers' from Amazon...")
    # هنا يجب وضع كود جلب البيانات أو استخدام API
    # سنضع قائمة افتراضية للمحاكاة
    best_sellers = ["Gaming Mechanical Keyboard", "Wireless Gaming Mouse", "Professional Studio Microphone"]
    product = random.choice(best_sellers)
    print(f"Agent A: Selected product: {product}")
    return product

# الوكيل B: الكتابة (تم تحسينه ليكون أكثر احترافية)
def agent_b_writer(product):
    return f"# Top Choice: {product}\n\n" \
           f"This {product} is currently trending as a top bestseller. " \
           f"It offers unparalleled performance and quality for professional users."

# الوكيل C: التنسيق مع رابطك reddobli-20
def agent_c_optimizer(draft, product):
    affiliate_link = "https://amzn.to/4dvQcZe?tag=reddobli-20"
    return draft + f"\n\n## Purchase Now\n[Click here to view {product} on Amazon]({affiliate_link})\n\n---\n*Keywords: BestSellers, {product.replace(' ', '')}, Recommended*"

# الوكيل D: النشر التلقائي
def agent_d_publisher(product, final_content):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{product.lower().replace(' ', '-')}.md"
    filepath = os.path.join("_posts", filename)
    
    if not os.path.exists("_posts"): os.makedirs("_posts")
        
    formatted = f"---\nlayout: post\ntitle: {product}\n---\n\n{final_content}"
    
    with open(filepath, "w") as f:
        f.write(formatted)
    
    os.system("git add .")
    os.system(f'git commit -m "Automated Post: {product}"')
    os.system("git push origin main")

# التنفيذ التلقائي (الآن لا يحتاج لمدخلات من المستخدم)
if __name__ == "__main__":
    product = agent_a_research()
    draft = agent_b_writer(product)
    final = agent_c_optimizer(draft, product)
    agent_d_publisher(product, final)
    print("Dobli Engine: Cycle completed successfully without manual intervention.")
