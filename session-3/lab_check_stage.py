import os

stage = os.getenv('STAGE', 'dev').upper()
output = f'We\'re running in {stage}'

if stage.startswith('PROD'):
    output = f'DANGER!!! - {output}'

print(output)
