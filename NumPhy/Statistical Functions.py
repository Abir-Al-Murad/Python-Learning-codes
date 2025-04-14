import numpy as np

a = np.array([1,2,3,4,5,6])
print("Mean(Average) of an Array\n",np.mean(a))
print("Median value of an Array\n",np.median([1,3,6,2,3,6,9,34])) #it frist sort the array than find the middle value
print("Standard Deviation of an Array\n",np.std(a))
print("Variance of an Array\n",np.var(a))
print("Minimum value of an Array\n",np.min(a))
print("Maximum value of an Array\n",np.max(a))

'''
variance:
    sigma^2 = (Summation of (Xi - mean)^2)/n
Standard Deviatin:
    sigma = sqrt of() (summation of (Xi - mean)^2)/n)

#!Variance (প্রসারণ) কী?
সংজ্ঞা:
Variance বা প্রসারণ হলো একটি ডাটাসেটের গড় (Mean) থেকে প্রতিটি উপাদান কত দূরে রয়েছে তার গড় স্কয়ারড দূরত্ব। এটি ডাটার ছড়িয়ে থাকার মাত্রা নির্দেশ করে।

কম Variance → ডাটা গড়ের কাছাকাছি।
বেশি Variance → ডাটা গড় থেকে বেশি দূরে ছড়িয়ে আছে।
📌 সরল ভাষায়: Variance বেশি হলে ডাটাগুলো বেশি পরিবর্তনশীল হবে, আর কম হলে ডাটাগুলো প্রায় কাছাকাছি থাকবে।

#! Standard Deviation (মানক বিচ্যুতি) কী?
সংজ্ঞা:
Standard Deviation হলো Variance-এর বর্গমূল। এটি ডাটার ছড়িয়ে পড়ার মাত্রা বোঝায়।

কম Standard Deviation → সংখ্যাগুলো গড়ের কাছাকাছি।
বেশি Standard Deviation → সংখ্যাগুলো গড় থেকে বেশি দূরে।

🔹 সংক্ষেপে
✔ Variance বেশি মানে ডাটা বেশি বিচ্ছিন্ন।
✔ Standard Deviation দিয়ে বুঝতে পারি ডাটাগুলো গড়ের চারপাশে কতটা ছড়ানো।
✔ Variance-এর বর্গমূল নিলেই Standard Deviation পাওয়া যায়।
'''


