#### Завдання 3 (20% балів + бонус).
Задано абстрактні базові клас Base1, Base2, і підкласи Base1: Alpha,
Beta та Base2: Gamma, Delta. Кожен екземпляр класів Base1, Base2 містить порядковий номер N
(унікальний для кожного підкласу, починається з 1 для першого створеного екземпляру, зростає на
1 для кожного наступного екземпляру), а також по одному вкладеному екземпляру класу Base1 та
по два екземпляри класу Base2. Деструктори класів змінюють глобальну змінну S:
- деструктор Base1: S = 3S + N + 41,
- деструктор Base2: S = S / 2 - N,
- деструктор Alpha: S = S - 2N + 14,
- деструктор Beta: S = S - N,
- деструктор Gamma: S = S - N,
- деструктор Delta: S = S + 3N - 41.
1. Реалізувати відповідні класи, створити і видалити певну кількість об’єктів, вивести
остаточне значення глобальної змінної.
2. Реалізувати функцію, яка буде отримувати список об’єктів і передбачати значення
глобальної змінної після послідовного видалення всіх цих об’єктів.
3. Для заданої кількості об’єктів M (що включає як незалежні, так і вкладені об’єкти)
перебрати всі можливі комбінації об’єктів, і вивести для кожного остаточне значення
змінної. Можна вважати M < 5.