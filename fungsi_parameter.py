def selamat(nama, waktu):
    print('selamat', waktu, nama, '......')


def greeting(name='tri', time='pagi'):  # with default parameter
    print('selamat', time, name, '......')


selamat('budi', 'pagi')
selamat('malam', 'andi')  # positional parameter
selamat(waktu='malam', nama='andi')  # named parameter
greeting()  # default parameter
greeting('rudi', 'petang')  # default parameter
