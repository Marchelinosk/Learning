# Mathematics Discrete
# Assignment 01

MARCHELINO SENDUK KAUNANG (10241040)

Silahkan memilih dua problem berikut untuk diselesaikan.

## Problem 2 (50 poin)
Secara lengkap ada 16 logika operator yang dapat digunakan untuk dua buah
proposisi $A$ dan $B$. Di pertemuan minggu ke-3 kita telah membahas
- konjungsi ($\wedge$)
- disjungsi ($\vee$)
- eksklusif XOR ($\oplus$)
- pernyataan bersyarat / implikasi ($\rightarrow$)
- bi-implikasi ($\leftrightarrow$)

Carilah sisa 11 operator logika yang lain dan berikan tabel kebenarannya. Mengapa ada beberapa operator logika yang tidak 
populer digunakan?

### Answer

Terdapat 11 operator logika yang dapat dapat kita gunakan, mengapa tidak populer banyak di gunakan banyak orang? Karena:
- **Keterpakaian Praktis**: Operator seperti AND, OR, dan NOT lebih sering digunakan dalam konteks sehari-hari, seperti pemrograman dan pengambilan keputusan. Operator lain, seperti XNOR atau NOR, mungkin lebih jarang muncul dalam aplikasi praktis.
- **Simplicity vs. Complexity**: Dalam banyak situasi, kita hanya perlu kombinasi sederhana dari kondisi, sehingga operator yang lebih kompleks seperti XOR atau XNOR tidak selalu diperlukan.
- **Familiaritas**: Banyak orang sudah terbiasa dengan operator dasar. Operator yang lebih kompleks bisa membuat analisis menjadi lebih rumit tanpa memberikan keuntungan yang signifikan.

**Dan berikut 11 Operator logika lainnya yang dapat digunakan.**

#### 1. **Negasi** ($\neg$ A)
 | A | $\neg$ A|
 | --| --------|
 | True | False|
 | False| True |

#### 2. **NAND** ( A $\uparrow$ B)
 | A | B |A $\uparrow$ B|
 |---|---| ------------ |
 | True  | True         | False |
 | True  | False        | True  |
 | False | True         | True  |
 | False | False        | True  |

#### 3. **NOR** ( A $\downarrow$ B)
 | A | B |A $\downarrow$ B|
 |---|---| ------------ |
 | True  | True         | False |
 | True  | False        | False |
 | False | True         | False |
 | False | False        | True  |

#### 4. **XNOR** ( A $\bigodot$ B)
 | A | B |A $\bigodot$ B|
 |---|---| ------------ |
 | True  | True         | True  |
 | True  | False        | False |
 | False | True         | False |
 | False | False        | True  |

#### 5. **A dan Bukan B** (A $\wedge$ $\neg$ B)
 | A | B |A $\wedge$ $\neg$ B|
 |---|---| ------------ |
 | True  | True         | False |
 | True  | False        | True  |
 | False | True         | False |
 | False | False        | False |

#### 6. **B dan Bukan A** (B $\wedge$ $\neg$ A)
 | A | B |B $\wedge$ $\neg$ A|
 |---|---| ------------ |
 | True  | True         | False  |
 | True  | False        | False  |
 | False | True         | True   |
 | False | False        | False  |

#### 7. **A atau Bukan B** (A $\vee$ $\neg$ B)
 | A | B |A $\vee$ $\neg$ B|
 |---|---| ------------ |
 | True  | True         | True  |
 | True  | False        | True  |
 | False | True         | False |
 | False | False        | True  |

#### 8. **B atau Bukan A** (B $\vee$ $\neg$ A)
 | A | B |A $\wedge$ $\neg$ B|
 |---|---| ------------ |
 | True  | True         | True  |
 | True  | False        | True  |
 | False | True         | True  |
 | False | False        | False |

#### 9. **A implikasi Bukan B** (A $\rightarrow$ $\neg$ B)
 | A | B |A $\wedge$ $\neg$ B|
 |---|---| ------------ |
 | True  | True         | False |
 | True  | False        | True  |
 | False | True         | True  |
 | False | False        | True  |

#### 10. **Bukan A implikasi B** ($\neg$ A $\rightarrow$ B)
 | A | B |$\neg$ A $\rightarrow$ B|
 |---|---| ------------ |
 | True  | True         | True |
 | True  | False        | False|
 | False | True         | True |
 | False | False        | True |

#### 11. **Bukan A implikasi Bukan B**($\neg$ A $\rightarrow $ $\neg$ B)
 | A | B |A $\wedge$ $\neg$ B|
 |---|---| ------------ |
 | True  | True         | False |
 | True  | False        | True  |
 | False | True         | False |
 | False | False        | True  |




## Problem 4 (40 poin)
Tentukan konvers, kontrapositive, dan invers dari
pernyataan kondisional berikut
1. Jika hari ini hujan, maka saya tidak akan datang ke
   kuliah matematika diskrit.
2. Saya akan belajar hingga jam dua dini hari, jika
   hari kemarin saya lupa untuk belajar.


### Answer 
#### 1. Jika hari ini hujan, maka saya tidak akan datang ke
   kuliah matematika diskrit.
  - $P$ = Hari ini Hujan
  - $Q$ = Saya tidak akan datang ke kuliah matematika diskrit

#### Notasi : $P$ $\rightarrow$ $Q$

#### a.Konvers

- Jika saya tidak akan datang ke kuliah matematika diskrit, maka hari ini hujan
- Notasi : $Q$ $\rightarrow$ $P$

#### b.Kontrapositive

- Jika saya datang ke kuliah matematika diskrit, maka hari ini cerah
- Notasi : $\neg$ $Q$ $\rightarrow$ $\neg$ $P$ 

#### c.Invers
- Jika hari ini cerah, maka saya datang ke kuliah matematika diskrit
- Notasi : $\neg$ $P$ $\rightarrow$ $\neg$ $Q$




#### 2. Saya akan belajar hingga jam dua dini hari, jika hari kemarin saya lupa untuk belajar.
 - R = Hari kemarin saya lupa untuk belajar
 - S = Saya akan belajar hingga jam dua dini hari

#### Notasi : $R$ $\rightarrow$ $S$

#### a.Konvers
- Jika Saya akan belajar hingga jam dua dini hari, maka kemarin saya lupa untuk belajar.
- Notasi : $S$ $\rightarrow$ $R$

#### b.Kontrapostive
- jika saya tidak belajar hingga jam dua dini hari, maka hari kemarin saya belajar.
- Notasi : $\neg$ $S$ $\rightarrow$ $\neg$ $R$

#### c.Invers
- Jika hari kemarin saya belajar, maka saya tidak akan belajar hingga jam dua dini hari.
- Notasi : $\neg$ $R$ $\rightarrow$ $\neg$ $S$










