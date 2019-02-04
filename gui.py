import PySimpleGUI as sg
import encryption
import decryption
import time


def main_event_loop():

    text_elements = ['encr_seed',
                     'plaintext',
                     'decr_seed',
                     'ciphertext',
                     'folder',
                     'file']

    button_elements = ['CLEAR ALL FIELDS',
                       'CLEAR ENCR. PASSWORD',
                       'ENCRYPT',
                       ' CLEAR PLAINTEXT ',
                       'CLEAR DECR. PASSWORD',
                       'DECRYPT',
                       'CLEAR CIPHERTEXT',
                       'CLEAR OUTPUT',
                       'FOLDER',
                       'FILE',
                       'ENCRYPT TO FILE',
                       'DECRYPT FROM FILE']

    window = sg.FlexForm('Crypt (v 1.0)', use_default_focus=False, icon="final_1")

    content = [[sg.ReadFormButton('CLEAR ALL FIELDS', key=button_elements[0]),
                sg.T('  (erase all text from screen)')],
               [sg.T('Encryption password:')],
               [sg.InputText(key=text_elements[0]), sg.T(' ' * 2),
                sg.ReadFormButton('CLEAR ENCR. PASSWORD', key=button_elements[1])],
               [sg.T('Message for encryption:')],
               [sg.Multiline(size=(160, 4), key=text_elements[1])],
               [sg.ReadFormButton('ENCRYPT', key=button_elements[2]),
                sg.ReadFormButton(' CLEAR PLAINTEXT ', key=button_elements[3])],
               [sg.Input(key=text_elements[4]), sg.FolderBrowse('FOLDER', key=button_elements[8])],
               [sg.ReadFormButton('ENCRYPT TO FILE', key=button_elements[10])],
               [sg.T('  ' + '_' * 158)],
               [sg.T('Decryption password:')],
               [sg.InputText(key=text_elements[2]), sg.T(' ' * 2),
                sg.ReadFormButton('CLEAR DECR. PASSWORD', key=button_elements[4])],
               [sg.T('Message for decryption:')],
               [sg.Multiline(size=(160, 4), key=text_elements[3])],
               [sg.ReadFormButton('DECRYPT', key=button_elements[5]),
                sg.ReadFormButton('CLEAR CIPHERTEXT', key=button_elements[6])],
               [sg.Input(key=text_elements[5]), sg.FileBrowse('FILE', key=button_elements[9])],
               [sg.ReadFormButton('DECRYPT FROM FILE', key=button_elements[11])],
               [sg.T('  ' + '_' * 158)],
               [sg.T('Output:')],
               [sg.Output(size=(160, 5))],
               [sg.ReadFormButton('CLEAR OUTPUT', key=button_elements[7])],
               [sg.SimpleButton('   Exit   ')]]

    window.LayoutAndRead(content, non_blocking=True)

    encryptor = encryption.Encryptor()
    decryptor = decryption.Decryptor()

    for i in range(1, 9999999999999999):

        button, values = window.ReadNonBlocking()

        if button == button_elements[0]:  # 'CLEAR ALL FIELDS'
            for element in text_elements:
                window.FindElement(element).Update('')
            for count in range(5):
                print('')

        elif button == button_elements[1]:  # 'CLEAR ENCR. PASS'
            window.FindElement(text_elements[0]).Update('')

        elif button == button_elements[2]:  # 'ENCRYPT'
            if values['plaintext'] != '\n' and values['encr_seed'] != '':
                msg = values['plaintext'].strip('\n')
                seed = values['encr_seed']
                encr_txt = encryptor.encrypt4(msg, seed)
                print(encr_txt)
            else:
                if values['plaintext'] == '\n':
                    print('No text provided for encryption...')
                if values['encr_seed'] == '':
                    print('No password provided for encryption...')

        elif button == button_elements[3]:  # 'CLEAR PLAINTEXT'
            window.FindElement(text_elements[1]).Update('')

        elif button == button_elements[4]:  # 'CLEAR DECR. PASS'
            window.FindElement(text_elements[2]).Update('')

        elif button == button_elements[5]:  # 'DECRYPT'
            if values['ciphertext'] != '\n' and values['decr_seed'] != '':
                txt = values['ciphertext'].strip('\n')
                print(txt)
                seed = values['decr_seed']
                decr_txt = decryptor.decrypt4(txt, seed)
                print(decr_txt)
            else:
                if values['ciphertext'] == '\n':
                    print('No text provided for decryption...')
                if values['decr_seed'] == '':
                    print('No password provided for decryption...')

        elif button == button_elements[6]:  # 'CLEAR CIPHERTEXT'
            window.FindElement(text_elements[3]).Update('')

        elif button == button_elements[7]:  # 'CLEAR OUTPUT'
            for count in range(5):
                print('')

        elif button == button_elements[10]:  # 'ENCRYPT TO FILE'
            output_loc = window.FindElement(text_elements[4]).Get()
            txt = values['plaintext'].strip('\n')
            seed = values['encr_seed']
            print('Encrypting...')
            encr_txt = encryptor.encrypt4(txt, seed)
            current_date = time.strftime("%d%m%Y")
            current_time = time.strftime("%I%M%S")
            date_and_time = current_date + '_' + current_time
            title = 'crypt_message_' + date_and_time + '.txt'
            with open(output_loc + '/' + title, 'w') as file:
                file.write(encr_txt)
            print('Successfully encrypted to file.')

        elif button == button_elements[11]:  # 'DECRYPT FROM FILE'
            if window.FindElement(text_elements[2]).Get() != '':
                encr_message = window.FindElement(text_elements[5]).Get()
                pswrd = window.FindElement(text_elements[2]).Get()
                with open(encr_message, 'r') as file:
                    x = file.read()
                decr_txt = decryptor.decrypt4(x, pswrd)
                print(decr_txt)
            else:
                print('You need to provide a password in the decryption password field.')

        if values is None or button == 'Exit':
            break

        file_text = window.Element('file').Get()
        window.Element('file').Update(file_text.split(sep='/')[-1].split(sep='.')[0])
        time.sleep(.01)

    else:
        window.CloseNonBlockingForm()


if __name__ == '__main__':
    main_event_loop()
