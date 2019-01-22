const rp = require('request-promise')
let fs = require('fs');

try {
    if (!fs.existsSync("./db")) fs.mkdirSync("./db");
    if (!fs.existsSync("./db/doc")) fs.mkdirSync("./db/doc");
    if (!fs.existsSync("./db/doc/item")) fs.mkdirSync("./db/doc/item");
    if (!fs.existsSync("./db/doc/item/en")) fs.mkdirSync("./db/doc/item/en");
    if (!fs.existsSync("./db/doc/item/en/3")) fs.mkdirSync("./db/doc/item/en/3");
} catch (error) {}

let doGet = (fileName,id) => {
    return new Promise(async (res, rej) => {
        try {
            let urrr = `http://www.garlandtools.org/${fileName}`
            let opt = {
                method: 'GET',
                url: urrr,
                timeout: 80 * 1000,
                gzip: true,
                headers: {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                    'Host': 'www.garlandtools.org',
                }
            }
            let data = await rp(opt)
            if (data.charCodeAt(0) == 65279)
                data = data.slice(1);
            fs.writeFileSync(`./${fileName}`, data)
            res(id)
        } catch (error) {
            rej({
                fileName: fileName,
                error: error
            })
        }
    })
}

/* get(urls[0]).then(data => {
    console.log(data)
}) */

let tableNotExist = (filename) => {
    // console.log(fs.existsSync(`.${filename}`))
    try {
        if (!fs.existsSync(`.${filename}`)) return true
        let data = fs.readFileSync(`.${filename}`, 'utf8');
        if (data.charCodeAt(0) == 65279)
            data = data.slice(1);
        let nodeObj = JSON.parse(data);
        return false
    } catch (error) {
        console.log(error)
        return true
    }
}
let index = 0
let times = 0
let data = JSON.parse(fs.readFileSync("../4.5/out/Item_en.json", 'utf8'))

let doit = () => {
    let all = []
    for (var i = 0; all.length < 10; i++) {
        index ++
        if (index > 45 && index <= 1600) continue //跳过 过期xxx
        if (data[index] === undefined) continue  //跳过不存在id
        if (data[index][0] === '') continue //跳过未实装数据
        var file = `/db/doc/item/en/3/${index}.json`
        if (tableNotExist(file)) {
            let a = doGet(file, index)
            all.push(a)
        }
    }
    // console.log(all)
    Promise.all(all).then(res => {
        console.log('Promise.all times=%s res= ', times, res)
        times++
        if (index <= Object.keys(data).length) {
            setTimeout(() => {
                doit()
            }, 2000)
        }
    }).catch((err) => {
        console.log('Promise.all err', err.length)
    })
}

doit()