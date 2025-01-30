# 🎬 Oscar-Web-Scraper  

## 📌 Description  
Oscar-Web-Scraper is a Python-based web scraping project that extracts data from the Wikipedia page listing **Academy Award-winning films**. The script retrieves details such as:  
- 🎥 **Film Name**  
- 📅 **Year of Award**  
- 🏆 **Number of Awards Won**  
- 🎖 **Number of Nominations**  

The scraped data is stored in a **Pandas DataFrame**, making it easy for analysis and visualization.  

---

## 🛠 Tech Stack  
- **Python** 🐍  
- `BeautifulSoup` – For web scraping  
- `Requests` – For fetching web content  
- `Pandas` – For data processing  
- `Matplotlib & Seaborn` – For data visualization (optional)  

---

## 🚀 Installation & Usage  

### 🔹 Prerequisites  
Ensure you have **Python 3.x** installed along with the required libraries:  

```bash
pip install numpy pandas matplotlib seaborn beautifulsoup4 requests
```

### 🔹 Clone the Repository  
```bash
git clone https://github.com/your-username/Oscar-Web-Scraper.git
cd Oscar-Web-Scraper
```

### 🔹 Run the Script  
```bash
python oscar_scraper.py
```

---

## 📊 Sample Output  
```
                Film   Year Awards Nominations
1363  Nomadland    2020    3        6
1364  CODA        2021    3        3
1365  Everything Everywhere All at Once  2022   7        11
```

---

## 📌 Features  
✅ **Automated Web Scraping** – Extracts Oscar-winning movie data from Wikipedia.  
✅ **Data Cleaning** – Removes unnecessary HTML tags and structures the data.  
✅ **Pandas Integration** – Stores data in a structured format for further analysis.  
✅ **Easy to Use** – Just run the script and get the latest Oscar-winning films.  

---

## 📝 License  
This project is licensed under the **MIT License**.  

---

## 👨‍💻 Contributing  
Contributions are welcome! Feel free to submit a pull request or open an issue.  

---

## ⭐ Support  
If you found this project useful, give it a ⭐ on GitHub!  

