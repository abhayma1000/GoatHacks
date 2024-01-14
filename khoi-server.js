const express = require ('express')
const app = express()
const port = 5000

app.use(express.static('public')) 
app.use(express.json()) 

app.get('/sell_offers', (req, res) => {
    res.status(200).json({info: 'hello my name is khoi'})
})

app.post('/', (req, res) => {
    const parcel = req.body
    console.log(parcel)
    if(!parcel) {
        return res.status(400).send({status: 'failed'})
    }
    res.status(200).send({status: 'recieved'}) 
})

app.listen(port, () => console.log('Server started on port: ' + port))
