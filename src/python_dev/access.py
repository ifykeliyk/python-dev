revoked_badges = {"P667", "A345", "W7723"}
approved = []
denied = []
while True:
    name = input("Enter person's name (or type 'done' to finish): ")
    if name.lower() == "done":
        break

    badge = input("Enter badge number: ").strip().upper()

    if badge in revoked_badges:
        denied.append(name)
        print(f"[ACCESS DENIED] {name} - Revoked badge")
    else:
        approved.append(name)
        print(f"[ACCESS GRANTED] {name}")

print("===== Access Summary =====")

print("Approved Visitors:")
for person in sorted(approved):
    print(f" - {person}")

print("Denied Visitors:")
for person in sorted(denied):
    print(f" - {person}")

print(f"Total Approved: {len(approved)}")
print(f"Total Denied: {len(denied)}")
