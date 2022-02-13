total_pages = int(input())
wanted_page = int(input())

flipped_times_from_start = 0
flipped_times_from_end = 0

start_page = 1
if total_pages % 2 == 0:
    end_page = total_pages
else:
    end_page = total_pages - 1

for i in range(1, wanted_page + 1):
    if start_page >= wanted_page:
        break
    else:
        start_page += 2
        flipped_times_from_start += 1

for i in range(total_pages, 0, -1):
    if end_page <= wanted_page:
        break
    else:
        end_page -= 2
        flipped_times_from_end += 1

print(min(flipped_times_from_end, flipped_times_from_start))
