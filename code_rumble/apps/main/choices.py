SENDING_METHODS = (
    ('sms', 'SMS'),
    ('email', 'email'),
)

ACCOUNT_TYPE = (('shipper', 'Shipper'),
                ('individual', 'I    ndividual'))

JOB_STATUS = (('new', 'new'),
              ('in_progess', 'In Progress'),
              ('delivered', 'delivered'))

PAYMENT_MODE = (
    ('bank_deposit', 'Bank Deposit'),
    ('eft', 'Electronic Funds Transfer'),
    ('cash', 'Cash'),
    ('card', 'Card'),
)

PAYMENT_STATUS = (
    ('pending', 'Pending'),
    ('complete', 'Complete'),
    ('declined', 'Declined'),
    ('reversed', 'Reversed'),
    ('confirmed', 'Confirmed'),
)

BID_STATUS = (
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('submited', 'Submitted'),
    ('under_consideration', 'Under Consideration')
)

BANK = (
    ('fnb', 'First National Bank'),
    ('bank_gaborone', 'Bank Gaborone'),
    ('stanbic', 'Stanbic Bank'),
    ('bank_abc', 'BancAbc'),
    ('bank_india', 'Bank Of India'),
    ('bank_baroda', 'Bank of Baroda'),
    ('standard_bank', 'Standard Bank'),
    ('baclays_bank', 'Baclays Bank'),
    ('western_union', 'Western Union'),
    ('pay_pal', 'Pay Pal'),
)

CARGO_TYPE = (
    ('harzard', 'Harzardous Material'),
    ('preshable', 'Perishables'),
    ('fragile', 'Fragile'),
    ('mechanical', 'Mechanical'),
)
