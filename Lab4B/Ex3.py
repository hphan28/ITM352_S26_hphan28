url = input("Enter a full URL: ")

clean_url = url.replace("https://", "")

print ("Cleaned URL:", clean_url)

parts = clean_url.split(".")

domain = parts[1]

print("Domain:", domain)

TLD= parts[2]

TLD_clean = TLD.strip("/")


top_level_domain = parts[2]

print("Top-Level Domain:", TLD_clean)

