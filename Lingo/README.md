# KQA Pro homepage

The website is hosted on Gitee. The url is <http://thukeg.gitee.io/kqa-pro/>.

## How to update the leaderboard
1. `cd pyscripts`
2. Open `leaderboard_data.csv` and append the data, including model information and accuracies
3. Run `python3 update_leaderboard.py`, it will reorganize the html code based on the latest data
4. Copy the output codes and insert them into proper position of `leaderboard.html`. There are comments in the html file for hint:
```
<!-- start open-ended data -->
    Paste open-ended codes here to override
<!-- end open-ended data -->
...

<!-- start multiple-choice data -->
    Paste multiple-choice codes here to override
<!-- end multiple-choice data -->
```

## How to edit the webpage

### Basic Usage

After downloading, simply edit the HTML and CSS files included with the template in your favorite text editor to make changes. These are the only files you need to worry about, you can ignore everything else! To preview the changes you make to the code, you can open the `index.html` file in your web browser.

### Advanced Usage

Run `npm install` and then run `npm start` which will open up a preview of the template in your default browser, watch for changes to core template files, and live reload the browser when changes are saved. You can view the `gulpfile.js` to see which tasks are included with the dev environment.
