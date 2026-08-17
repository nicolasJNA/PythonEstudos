import locale
import calendar

locale.setlocale(locale.LC_ALL,'')

print(calendar.calendar(2026))

print(locale.getlocale())