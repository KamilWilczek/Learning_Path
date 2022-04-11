## Krok 1 - import bibliotek

# generuje stempel czasowy
import datetime
# contains hash algorithm
import hashlib

## krok 2 - utworzenie bloku

# definicja struktury danych dla bloku
class Block:
    # każdy blok posiada 7 parametrów

    #1 numer bloku - pierwszy inicjalizujemy wartością 0
    blockNo = 0
    #2 jakie dane zapisujemy w bloku
    data = None # inicjalizacja wartością None
    #3 zmienna wskazująca na kolejny blok
    next = None
    #4 Wartość hash dla tego bloku (obsługuje unikalne ID i odpowiada za weryfikację jego integralności
    # Hash to funkcja, która konwertuje dane na liczbę w określonym zakresie
    hash = None
    #5 Liczba użyta tylko raz pomaga nam obliczyć hash bloku
    nonce = 0 # wartość tymczasowa
    #6 przechowuje ID hashu poprzedniego bloku z łańcucha bloków
    previous_hash = 0x0 # wartość inicjalizacyjna
    #7 stempel czasu
    timestamp = d

    #inicjalizacja bloku wpisując dane do jego wnętrza
    def __init__(self, data):
        self.data = data

    def hash(self):
            #SHA-256 to algorytm hashujący, który generuje unikalny 256-bitowy podpis, który jest określonym tekstem
        h = hashlib.sha256()

        #wejscem dla algorytmu SHA-256 będzie połączony string składający się z 5 atrybutów bloku: the temp, data, previous hash, timestamp i block
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        #zwraca 'hexadecimal string'
        return h.hexdigest()

    def __str__(self):
        # wyświetl dane bloku
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " str(self.nonce) + "\n--------------------"

## Krok 3 - utwórz blockchain

#definicja struktury danych dla blockchain składa się z bloków połączonych ze sobą w celu stworzenia łańcucha.
class Blockchain:

    #trudność kopania bloków
    diff = 20
    #2^32. jest to maksymalna liczba jaką można przechowywać w 32-bitach
    maxNonce = 2**32
    #docelowy hash
    target = 2 ** (256-diff)

    #generuje pierwszy blok w blockchain, genesis block
    block = Block("Genesis")
    #ustawienie tego bloku jako pierwszego w łańcuchu
    head = block

    #dodawanie bloku do łańcucha bloków
    def add(self, block):
        #ustawienie hash danego bloku jako nowy hash poprzedniego bloku
        block.previous_hash = self.block.hash()
        #ustaw hash bloku naszego nowego bloku jako # danego bloku + 1
        block.blockNo = self.block.blockNo + 1

        #ustawiamy wartość
        self.block.next = block
        self.block = self.block.next
