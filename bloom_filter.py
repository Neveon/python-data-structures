import pyhash

# bloom filters are like hash tables however save space
# there are false positives with bloom filters but no false negatives
# bloom filter example with pokemon pokedex
bit_vector = [0] * 20

# non cryptographic hash functions (Murmur and FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# pikachu -> FNV -> numbers that correspond to indice of bit vector

# Calculate the output of FNV and Murmur hash functions for Pikachu and Charmander
fnv_pika = fnv('Pikachu') % 20 # modulo used because we are using a bit vector of size 20
fnv_char = fnv('Charmander') % 20
murmur_char = murmur('Charmander') % 20
murmur_pika = murmur('Pikachu') % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1
bit_vector[murmur_char] = 1
bit_vector[fnv_char] = 1

