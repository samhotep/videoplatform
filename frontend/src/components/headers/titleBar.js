import React from "react";
import TitleItem from '../../components/menuItems/titleItem';
import TitleList from '../../components/menuItems/titleList';
import SearchButton from '../../components/menuItems/searchButton';
import styled from 'styled-components';

function TitleBar(props){
    return (
        <TitleContainer>
            <TitleItem name="Home"/>
            <SearchButton/>
        </TitleContainer>
    )
}

/*
            <TitleList name="Categories"/>
            
*/

const TitleContainer = styled.div`
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: 100vw;
    background-color: #7f0000;
`

export default TitleBar;
