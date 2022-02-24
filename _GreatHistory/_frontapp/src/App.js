import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import Header from "./components/Header";
import Footer from "./components/Footer";
import UserList from "./components/UserList";
import Main from "./components/Main";
import CategoryList from "./components/CategoryList";
import axios from "axios";
import LoginForm from "./components/LoginForm";
import RegisterForm from "./components/RegisterForm";

const API_URL = "http://127.0.0.1:8080";
const getResourceURL = (suffix) => `${API_URL}/api/${suffix}/`;


class App extends React.Component {
    constructor(props) {
        super(props);  // parent constructor
        this.state = {
            users: [],
            categories: [],
            accessToken: this.getAccessToken(),
        };
        // bind
    }

    componentDidMount() {
        this.loadState()
    }

    loadState() {
        let headers = this.getHeaders();

        // call rest API
        axios
            .get(getResourceURL("users"), {headers: headers})
            .then((result) => {
                // console.log('users result:', result)
                this.setState({
                    users: result.data
                })
            })
            .catch((error) => console.log(error));
        axios
            .get(getResourceURL("categories"), {headers: headers})
            .then((result) => {
                this.setState({
                    categories: result.data
                })
            })
            .catch((error) => console.log(error));

    }

    login(username, password) {
        // console.log('do login', username, password);
        axios
            .post(getResourceURL("token"),
                {"username": username, "password": password})
            .then((result) => {
                let refreshToken = result.data.refresh;
                let accessToken = result.data.access;
                console.log(accessToken)

                this.saveTokens(refreshToken, accessToken)
                this.setState({accessToken: accessToken}, this.loadState)
            })
            .catch((error) => console.log(error));
    }

    register(username, password1, password2, email) {
        console.log('do register', username, password1, password2, email);
        // axios
        //     .post(getResourceURL("token"),
        //         {"username": username, "password": password})
        //     .then((result) => {
        //         let refreshToken = result.data.refresh;
        //         let accessToken = result.data.access;
        //         console.log(accessToken)
        //
        //         this.saveTokens(refreshToken, accessToken)
        //         this.setState({accessToken: accessToken}, this.loadState)
        //     })
        //     .catch((error) => console.log(error));
    }

    logout() {
        // console.log('do logout');
        localStorage.setItem('refreshToken', null);
        localStorage.setItem('accessToken', null);
        this.clearState();
    }

    clearState() {
        this.setState({
            accessToken: null,
            users: [],
            categories: [],
        })
    }

    saveTokens(refreshToken, accessToken) {
        localStorage.setItem('refreshToken', refreshToken);
        localStorage.setItem('accessToken', accessToken);
    }

    getAccessToken() {
        return localStorage.getItem('accessToken')
    }

    isAuthenticated() {
        return this.state.accessToken !== 'null' && this.state.accessToken !== null;
    }

    getHeaders() {
        let headers = {
            'Content-Type': "application/json"
        }
        if (this.isAuthenticated()) {
            headers['Authorization'] = `Bearer ${this.state.accessToken}`
        }

        return headers;
    }

    render() {
        // console.log('state', this.state);
        return (
            <div className="main">
                <Router>
                    <Header isAuthenticated={this.isAuthenticated()}
                            logout={() => this.logout()}/>
                    <Route exact path="/">
                        <Main/>
                    </Route>
                    <Route exact path="/users">
                        <UserList users={this.state.users}/>
                    </Route>
                    <Route exact path="/categories">
                        <CategoryList categories={this.state.categories}/>
                    </Route>
                    <Route exact path="/login">
                        <LoginForm
                            login={(username, password) => this.login(username, password)}/>
                    </Route>
                    <Route exact path="/register">
                        <RegisterForm
                            register={(username, password1, password2, email) =>
                                this.register(username, password1, password2, email)}/>
                    </Route>
                </Router>
                <Footer/>
            </div>
        )
    }
}

export default App;
