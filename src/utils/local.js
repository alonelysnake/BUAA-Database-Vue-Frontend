// localStorage 缓存机制，报告和申优可写
const LOCAL_STORAGE_KEY = "searchHistory";

class Local { }

Local.saveHistory = (arr) => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(arr));
}

Local.loadHistory = () =>JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY))

Local.removeAllHistory=()=>{localStorage.removeItem(LOCAL_STORAGE_KEY)}


module.exports = Local
