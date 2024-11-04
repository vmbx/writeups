from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
    rotors='I II III',
    reflector='B',
    ring_settings='D D D',
    plugboard_settings='AG BH'
)

machine.set_display('ABC') 

ciphertext = "ymnjp znmjo gteqj cjwwh qljtd nprmp g".replace(" ", "")

plaintext = machine.process_text(ciphertext)

print("Decrypted message:")
print(plaintext)

# OUTPUT: BERLINHADSECRETSBENEATHHISCHARM
# Flag: QUESTCON{BERLIN_HAD_SECRETS_BENEATH_HIS_CHARM}
