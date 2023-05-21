# 백엔드 프론트엔드 연결

# 장고 시작 
pip install django-rest-framework

rom django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductList(APIView):
  def get(self, request):
    products = Product.objects.all()
    return Response(products.to_json())
  
#axios lib
import React from 'react';
import ReactDOM from 'react-dom';

import axios from 'axios';

class App extends React.Component {
    state = {
        users: []
    };

    componentDidMount() {
        axios.get('https://example.com/api/v1/users')
            .then((response) => response.data)
            .then((users) => this.setState({ users }));
    }

    render() {
        return (
            <div>
                <h1>Users</h1>
                <ul>
                    {this.state.users.map((user) => (
                        <li key={user.id}>{user.name}</li>
                    ))}
                </ul>
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));    

 # 불러오기 ? 
 import requests

def get_api_data(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception('API request failed')

# front 
const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const getApiData = async () => {
      try {
        const response = await get_api_data('https://api.example.com/data');
        setData(response);
      } catch (error) {
        console.error(error);
      }
    };

    getApiData();
  }, []);

  return (
    <div>
      <h1>API Data</h1>
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
};

export default App;
#2 
const fetchData = async () => {
    try {
      setError(null);
      setData(null);
      setLoading(true);

      const response = await axios.get(URL, {
        params: {
          serviceKey: process.env.REACT_APP_API_KEY,
          numOfRows: 1,
          pageNo: 10
        }
      });

      setData(response.data);
    } catch(e) {
      setError(e);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);
  
  if(loading) return <div>Loading...</div>;
  if(error)   return <div>Error...</div>;
  if(!data)   return null;
  
# python connect html
# json -> html 

def json_to_html(json_data):
    html = ""
    for key, value in json_data.items():
        html += "<p><strong>{0}:</strong> {1}</p>".format(key, value)
    return html
  
  html_data = json_to_html(json_data)
  
  
  
