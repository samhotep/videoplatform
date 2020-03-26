import React from "react";
import styled from 'styled-components';

function TitleItem(props){
    return (
        <Item>
            {props.name}
        </Item>
    )
}

const Item = styled.div`
    padding: 10px;
    margin: 10px;
    color: white;

    &:hover {
        background-color: #b71c1c;
    }
`

export default TitleItem;
