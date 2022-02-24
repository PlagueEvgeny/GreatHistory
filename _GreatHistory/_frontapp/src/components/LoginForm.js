import React from "react";


class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        };
    }

    handleChange(event) {
        this.setState(
            {[event.target.name]: event.target.value}
        )

    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.login(this.state.username, this.state.password);
    }

    render() {
        return (
            <div className="login-form">
                <form method="post"
                      onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text"
                           name="username"
                           placeholder="username"
                           onChange={(event) => this.handleChange(event)}/>
                    <input type="password"
                           name="password"
                           placeholder="password"
                           onChange={(event) => this.handleChange(event)}/>
                    <input type="submit"
                           value="login"/>
                </form>
            </div>
        )
    }

}

export default LoginForm
