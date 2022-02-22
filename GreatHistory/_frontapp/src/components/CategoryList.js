import {NavLink as Link} from "react-router-dom";
import React from "react";

const Category = ({category}) => {
    // console.log('project:', project);
    return (
        <tr className="project-row">
            <td>
                {category.id}
            </td>
            <td>
                <Link to={`/categories/detail/${category.id}`} className="nav-link">
                        {category.name}
                </Link>
            </td>
            <td>
                {category.desc}
            </td>
            <td>
                <Link to={`/categories/delete/${category.id}`} className="nav-link">
                        delete
                </Link>
            </td>
        </tr>
    )
}

const CategoryList = ({categories}) => {
    // console.log('projects:', projects);
    // this.props.projects
    return (
        <div className="project-list">
            <h1>Categories</h1>
            <table className="project-list__table">
                <thead>
                <tr>
                    <th>id</th>
                    <th>name</th>
                    <th>desc</th>
                </tr>
                </thead>
                <tbody>
                {categories.map((category) => <Category key={category.id} category={category}/>)}
                </tbody>
            </table>
        </div>
    )
}

export default CategoryList;