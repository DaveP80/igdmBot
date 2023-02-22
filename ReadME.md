### IG Bot

![davidpaquette](https://i.imgur.com/bdoFM1H.png)
![pythondavep](https://i.imgur.com/9sTPYBa.png)

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
### if you want to pull data from a google sheets doc
> get your i.am service account json file from google.

### otherwise, just use a local csv file.

I recommend lines 51 thru 74, refactor, because you don't need as many conditionals
to get it to run the first time. just rely on 'queryBox' selector.

.env contains secret variables

put your full path for your credentials.json in the creds variable.

alter update_cell to the shape of your sheets document.