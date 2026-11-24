from pyscript import display, document

def add_member(e):
    document.getElementById('output1').innerHTML = ""

    club_members_g8 = {'Zeth Barbadillo', 'Sofia Violago', 'Nathalie Pineda'}
    club_members_g9 = {'Kristel Esguerra', 'Khloe Gutierrez', 'Zoey Adlawan'}
    club_members_g10 = {'Hope Benitez', 'Julienne Miranda', 'Johanna Ramos'}
    club_members_g11 = {'Jamie Castelo', 'Sam Luna', 'Janine Mariposque'}

    new_mem_first = document.getElementById('fname').value
    new_mem_last = document.getElementById('lname').value

    new_mem_full = new_mem_first.title() + " " + new_mem_last.title()
    new_mem_fullset = {new_mem_full}

    all_mem = club_members_g8 | club_members_g9 | club_members_g10 | club_members_g11 | new_mem_fullset

    total_mem = len(club_members_g8 | club_members_g9 | club_members_g10 | club_members_g11 | new_mem_fullset)

    mem_list = "<br>".join(sorted(all_mem))
    
    #display
    document.getElementById('output1').innerHTML = f'<b>All Members:</b> <br>{mem_list}<br><br>'
    display(f'Total members: {total_mem}', target="output1")