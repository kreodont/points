import gql from 'graphql-tag'

export default gql`
    query {allPoint{points{points_owner{printable_name, current_points}, details, number}}}
    `
