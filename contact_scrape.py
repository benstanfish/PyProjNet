from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file=file_path) as doc:
    soup = BeautifulSoup(doc, 'html.parser')


table_cells = soup.find_all('td')
names = [i.find('a').contents[0].title() for i in table_cells if i.find('a') != None]
emails = [i.find('a').attrs['href'].replace('mailto:','').lower() for i in table_cells if i.find('a') != None]
departments = [i.next_sibling.next_sibling.contents[0] for i in table_cells if i.find('a') != None]
phones = [i.next_sibling.next_sibling.next_sibling.next_sibling.contents[0] for i in table_cells if i.find('a') != None]

contacts = [(names[i], emails[i], departments[i], phones[i]) for i in range(0, len(names))]   

unique_contacts = []

for contact in contacts:
    if contact not in unique_contacts:
        unique_contacts.append(contact)

unique_contacts.sort()
    
with open('output.txt', 'w') as f:
    for contact in unique_contacts:
        f.write('\t'.join(contact) + '\n')