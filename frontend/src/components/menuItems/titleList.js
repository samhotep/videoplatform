import React from "react";
import styled from 'styled-components';

function TitleList(props){
    return (
        <div>
            <select style={styles.container}>
                <option defaultValue={props.name}>{props.name}</option>
                <option value="Random">Random</option>
            </select>
        </div>
    )
}

const styles = {
    container: {
        backgroundColor: '#850127',
        padding: 10,
        margin: 10,
        borderWidth: 0,
    }
}

export default TitleList;
