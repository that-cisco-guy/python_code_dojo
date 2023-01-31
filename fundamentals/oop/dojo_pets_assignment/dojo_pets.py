import ninjas
import pets


Michaelangelo = pets.Pet('Michaelangelo', 'ninja turtle', 'master of nunchucks', 'HIYA!' )
Mufasa = pets.Cat('Mufasa', 'lion', 'bite your face off', 'ROAR!')


RedNinja = ninjas.Ninja('Red', 'Ninja', Michaelangelo, 'lettuce', 'pizza' )
BlueNinja = ninjas.Ninja('Red', 'Ninja', Mufasa, 'lettuce', 'pizza' )


RedNinja.feed()
RedNinja.walk()
RedNinja.bathe()

BlueNinja.feed()
BlueNinja.walk()
BlueNinja.bathe()
BlueNinja.is_king()
