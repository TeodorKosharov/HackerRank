def fun(s: str):
    try:
        username, url = s.split('@')
        site_name, extension = url.split('.')
    except ValueError:
        return False

    # username checking:
    username_results = [True if x.isalnum() or x == '_' or x == '-' else False for x in username]
    if False in username_results or len(username) == 0:
        return False

    # site name checking:
    site_name_results = [True if x.isalnum() else False for x in site_name]
    if False in site_name_results:
        return False

    # extension checking:
    extension_results = [True if x.isalpha() else False for x in extension]
    if False in extension_results or len(extension) > 3:
        return False

    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
